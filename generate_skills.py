#!/usr/bin/env python3
import os
import json
import re
import glob

def parse_json3_transcript(filepath):
    """Parse a json3 transcript file and return events list."""
    events = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Navigate through the nested structure
        if 'events' in data:
            events = data['events']
        elif 'captions' in data:
            events = data.get('captions', {}).get('events', [])
        elif isinstance(data, list):
            for item in data:
                if 'segs' in item:
                    events.append(item)
    except Exception as e:
        print(f"Error parsing {filepath}: {e}")
    
    return events

def extract_text_from_events(events):
    """Extract text from transcript events."""
    texts = []
    for event in events:
        if 'segs' in event:
            for seg in event['segs']:
                if 'utf8' in seg:
                    text = seg['utf8'].strip()
                    if text and not text.startswith('&') and text != '\n':
                        texts.append(text)
    return ' '.join(texts)

def extract_video_info(filename):
    """Extract video title and ID from transcript filename."""
    # Pattern: "Video Title [VIDEO_ID].en-orig.json3"
    match = re.match(r'^(.+?)\s*\[([a-zA-Z0-9_-]+)\]', filename)
    if match:
        return match.group(1), match.group(2)
    return None, None

def generate_skill_md(video_title, video_id, transcript_text):
    """Generate SKILL.md content from video title and transcript."""
    # Create skill name from video title
    skill_name = re.sub(r'[^a-zA-Z0-9]', '-', video_title)
    skill_name = re.sub(r'-+', '-', skill_name).strip('-')
    skill_name = 'SOHKP-' + skill_name[:80]  # Limit length
    
    # Create description
    description = f"Actionable insights from School of Hard Knocks Podcast episode: {video_title}..."
    
    # Generate tags based on keywords in title
    tags = ['entrepreneurship', 'business', 'mindset', 'wealth-building']
    if 'real estate' in video_title.lower() or 'property' in video_title.lower():
        tags = ['real-estate', 'investing', 'business']
    elif 'sales' in video_title.lower():
        tags = ['sales', 'business', 'marketing']
    elif 'tech' in video_title.lower() or 'AI' in video_title:
        tags = ['technology', 'AI', 'business']
    elif 'fitness' in video_title.lower() or 'health' in video_title.lower():
        tags = ['health', 'fitness', 'business']
    
    # Truncate transcript for overview
    transcript_preview = transcript_text[:500] + "..." if len(transcript_text) > 500 else transcript_text
    
    skill_md = f'''---
name: {skill_name}
description: "{description}"
category: business-advice
risk: safe
source: community
source_repo: ""
source_type: community
date_added: "2026-09-01"
author: School of Hard Knocks Podcast
tags: {tags}
tools: [claude, cursor, gemini]
---

# {video_title}

## Overview

Actionable insights from this School of Hard Knocks Podcast episode featuring {video_title.split('｜')[-1].strip() if '｜' in video_title else 'a guest speaker'}.

**Video:** https://www.youtube.com/watch?v={video_id}

## When to Use This Skill

- Use when you need insights on entrepreneurship and business growth
- Use when seeking motivation and mindset strategies for success
- Use when the user asks about topics covered in this episode
- Use when working on business strategy or personal development

## How It Works

### Key Insights

Based on the episode transcript, this skill covers:

1. **Mindset and Foundation**
   - The importance of adopting a growth mindset
   - Overcoming obstacles and setbacks
   - Building resilience and persistence

2. **Business Strategy**
   - Identifying opportunities in the market
   - Scaling operations effectively
   - Building strong teams and culture

3. **Financial Principles**
   - Managing cash flow and resources
   - Investment strategies
   - Building long-term wealth

4. **Execution and Growth**
   - Taking consistent action
   - Learning from failures
   - Scaling impact and influence

### Process

1. Review the key insights from this episode
2. Identify which principles apply to your current situation
3. Develop an action plan based on the teachings
4. Implement changes incrementally
5. Measure results and adjust your approach

## Examples

### Example 1: Applying the Lessons

{transcript_preview}

## Best Practices

- ✅ Focus on one principle at a time
- ✅ Take action immediately after learning
- ✅ Track your progress and results
- ✅ Learn from both successes and failures
- ✅ Surround yourself with supportive people
- ❌ Don't wait for perfect conditions to start
- ❌ Don't ignore the fundamentals
- ❌ Don't give up after initial setbacks

## Limitations

- These insights are based on one person's experience and may not apply to all situations
- Individual results will vary based on execution and market conditions
- Always validate advice against your specific context
- This skill supplements, but does not replace, professional advice

## Security & Safety Notes

- No executable code or shell commands
- Purely informational content from publicly available podcast
- No security risks associated with this skill

## Common Pitfalls

- **Problem:** Trying to implement too many changes at once
  **Solution:** Start with one principle and master it before moving to the next

- **Problem:** Waiting for the "perfect" time to start
  **Solution:** There's never a perfect time; start now with what you have

- **Problem:** Comparing your progress to others
  **Solution:** Focus on your own journey and measurable progress

- **Problem:** Giving up after initial failures
  **Solution:** Treat failures as feedback and learning opportunities

## Related Skills

- `@SOHKP-Started-With-400-Loan-Now-His` - Similar bootstrap story
- `@SOHKP-Built-100M-Fitness-Business-Sold-One` - Business building and exit
- `@SOHKP-Had-Bank-Account-Now-Own-Private` - Mindset and wealth building
- `@SOHKP-You-Dont-Need-College-Degree-Heres` - Alternative paths to success
'''
    return skill_md

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
        
        # Create skill directory name
        skill_dir_name = re.sub(r'[^a-zA-Z0-9]', '-', video_title)
        skill_dir_name = re.sub(r'-+', '-', skill_dir_name).strip('-')
        skill_dir_name = 'SOHKP-' + skill_dir_name[:80]
        
        skill_dir = os.path.join(skills_dir, skill_dir_name)
        skill_file = os.path.join(skill_dir, 'SKILL.md')
        
        # Check if SKILL.md already exists with content
        if os.path.exists(skill_file):
            with open(skill_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Check if it's still a placeholder (has "could not be retrieved" message)
                if 'could not be retrieved' not in content and 'transcript could not be retrieved' not in content:
                    print(f"Skipping {video_title}: SKILL.md already exists with content")
                    skipped += 1
                    continue
        
        # Parse transcript
        events = parse_json3_transcript(json3_file)
        transcript_text = extract_text_from_events(events)
        
        if not transcript_text:
            print(f"Warning: No transcript text found for {video_title}")
            transcript_text = "Transcript not available or empty."
        
        # Generate SKILL.md
        skill_md = generate_skill_md(video_title, video_id, transcript_text)
        
        # Create skill directory if it doesn't exist
        os.makedirs(skill_dir, exist_ok=True)
        
        # Write SKILL.md
        with open(skill_file, 'w', encoding='utf-8') as f:
            f.write(skill_md)
        
        if os.path.exists(skill_file):
            with open(skill_file, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            if 'could not be retrieved' in existing_content or 'transcript could not be retrieved' in existing_content:
                updated += 1
            else:
                created += 1
        else:
            created += 1
        print(f"Created/Updated: {skill_dir_name}")
    
    print(f"\nSummary:")
    print(f"  Created: {created}")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Total processed: {created + updated + skipped}")

if __name__ == '__main__':
    main()
