#!/usr/bin/env python3
import os
import json
import re
import glob

def parse_json3_transcript(filepath):
    """Parse a json3 transcript file and return full text."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        events = data.get('events', [])
        texts = []
        for event in events:
            if 'segs' in event:
                for seg in event['segs']:
                    if 'utf8' in seg:
                        text = seg['utf8'].strip()
                        if text and not text.startswith('&'):
                            texts.append(text)
        return ' '.join(texts)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
        return ""

def extract_video_info(filename):
    """Extract video title and ID from transcript filename."""
    match = re.match(r'^(.+?)\s*\[([a-zA-Z0-9_-]+)\]', filename)
    if match:
        return match.group(1), match.group(2)
    return None, None

def generate_money_teaching_md(video_title, video_id, transcript_text):
    """Generate MONEY-TEACHING.md content from video title and transcript."""
    # Create directory name from video title
    dir_name = re.sub(r'[^a-zA-Z0-9]', '-', video_title)
    dir_name = re.sub(r'-+', '-', dir_name).strip('-')
    dir_name = 'SOHKP-' + dir_name[:80]
    
    # Create description from transcript
    description = f"This money teaching distills the key financial and business principles from '{video_title}' into actionable steps you can apply to build wealth and achieve financial freedom."
    
    # Extract key insights from transcript
    # Look for actionable phrases and patterns
    insights = []
    sentences = re.split(r'(?<=[.!?])\s+', transcript_text)
    
    # Look for specific patterns
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 20 or len(sentence) > 300:
            continue
        
        # Look for actionable content
        if any(keyword in sentence.lower() for keyword in [
            'you need to', 'the way to', 'how to', 'step', 'first', 'second', 'third',
            'important', 'critical', 'key', 'strategy', 'principle', 'rule',
            'always', 'never', 'make sure', 'focus on', 'avoid', 'stop',
            'start', 'begin', 'build', 'create', 'invest', 'save', 'spend',
            'million', 'billion', 'success', 'fail', 'mistake', 'lesson'
        ]):
            insights.append(sentence)
    
    # Use first few meaningful insights
    key_insights = insights[:10] if insights else sentences[:5]
    
    # Generate steps from insights
    steps = []
    for i, insight in enumerate(key_insights[:5], 1):
        steps.append(f"### Step {i}: {insight[:60].title()}\n\n{insight}")
    
    steps_md = '\n\n'.join(steps) if steps else "### Step 1: Learn the Principles\n\nExtract the key principles from this episode and apply them to your financial journey."
    
    # Generate examples
    examples_md = f"""### Example 1: Applying the Lessons

The speaker shared their personal experience: {key_insights[0] if key_insights else 'N/A'}

### Example 2: Real-World Application

Consider how these principles can be applied to your own financial situation and business ventures."""
    
    # Best practices
    best_practices = """- ✅ Focus on consistent action rather than perfect planning
- ✅ Build multiple income streams to diversify your wealth
- ✅ Invest in yourself and your education first
- ✅ Surround yourself with people who challenge and support you
- ✅ Track your progress and adjust your strategies as needed
- ❌ Don't rely on a single source of income
- ❌ Don't let fear of failure prevent you from taking action
- ❌ Don't ignore the fundamentals of financial management"""
    
    # Keep in mind
    keep_in_mind = """- Every situation is unique; adapt these principles to your context
- Results require time and consistent effort
- The journey to wealth is rarely linear
- Continuous learning is essential for long-term success"""
    
    # Security & Safety Notes
    security_notes = """- This is educational content based on publicly available podcast episodes
- Always do your own research before making financial decisions
- Consider consulting with qualified financial advisors for personalized advice
- Never invest more than you can afford to lose"""
    
    # Common pitfalls
    common_pitfalls = """- **Problem:** Waiting for the "perfect" time to start
  **Solution:** Start now with what you have; perfect timing doesn't exist

- **Problem:** Trying to get rich quick without putting in the work
  **Solution:** Focus on building sustainable wealth through consistent effort

- **Problem:** Comparing your progress to others
  **Solution:** Focus on your own journey and measurable progress

- **Problem:** Giving up after initial setbacks
  **Solution:** Treat failures as feedback and learning opportunities"""
    
    # Generate examples from transcript
    example_texts = []
    for i, insight in enumerate(key_insights[:3], 1):
        example_texts.append(f"**Example {i}:** {insight}")
    
    examples_md = '\n\n'.join(example_texts) if example_texts else "**Example 1:** Apply the principles from this episode to your own business or investment strategy."
    
    money_teaching_md = f"""# {video_title}

## Overview

{description}

**Video:** https://www.youtube.com/watch?v={video_id}

## When to Follow These Money Teachings

- When you need guidance on building wealth and financial independence
- When working on business growth and scaling strategies
- When seeking motivation and practical advice from successful entrepreneurs
- When the user asks about topics covered in this episode

## Steps

{steps_md}

## Examples

{examples_md}

## Best Practices

{best_practices}

## Keep In Mind

{keep_in_mind}

## Security & Safety Notes

{security_notes}

## Common Pitfalls

{common_pitfalls}
"""
    return dir_name, money_teaching_md

def main():
    transcript_dir = os.getcwd()
    skills_dir = "/workspace/0a976afa-9d91-494d-85d2-5832b5541cb3/sessions/agent_e738659b-7c08-4768-85ed-8bd73d9fd778/.kilo/skills"
    
    # Find all json3 files
    json3_files = glob.glob(os.path.join(transcript_dir, '*.json3'))
    print(f"Found {len(json3_files)} transcript files")
    
    created = 0
    updated = 0
    skipped = 0
    
    for json3_file in sorted(json3_files):
        filename = os.path.basename(json3_file)
        video_title, video_id = extract_video_info(filename)
        
        if not video_title or not video_id:
            print(f"Skipping {filename}: could not parse video info")
            skipped += 1
            continue
        
        # Create directory name
        dir_name = re.sub(r'[^a-zA-Z0-9]', '-', video_title)
        dir_name = re.sub(r'-+', '-', dir_name).strip('-')
        dir_name = 'SOHKP-' + dir_name[:80]
        
        skill_dir = os.path.join(skills_dir, dir_name)
        teaching_file = os.path.join(skill_dir, 'MONEY-TEACHING.md')
        
        # Check if MONEY-TEACHING.md already exists
        if os.path.exists(teaching_file):
            with open(teaching_file, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'MONEY-TEACHING.md' in content or '# ' in content:
                    print(f"Skipping {video_title}: MONEY-TEACHING.md already exists")
                    skipped += 1
                    continue
        
        # Parse transcript
        transcript_text = parse_json3_transcript(json3_file)
        
        if not transcript_text:
            print(f"Warning: No transcript text found for {video_title}")
            transcript_text = "Transcript not available."
        
        # Generate MONEY-TEACHING.md
        _, teaching_md = generate_money_teaching_md(video_title, video_id, transcript_text)
        
        # Create directory if it doesn't exist
        os.makedirs(skill_dir, exist_ok=True)
        
        # Write MONEY-TEACHING.md
        with open(teaching_file, 'w', encoding='utf-8') as f:
            f.write(teaching_md)
        
        # Remove old SKILL.md if it exists
        old_skill_file = os.path.join(skill_dir, 'SKILL.md')
        if os.path.exists(old_skill_file):
            os.remove(old_skill_file)
        
        created += 1
        print(f"Created: {dir_name}/MONEY-TEACHING.md")
    
    print(f"\nSummary:")
    print(f"  Created: {created}")
    print(f"  Skipped: {skipped}")
    print(f"  Total processed: {created + skipped}")

if __name__ == '__main__':
    main()
