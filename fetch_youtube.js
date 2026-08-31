const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch({
      headless: 'new',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--ignore-certificate-errors']
    });
    const page = await browser.newPage();
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36');
    await page.goto('https://www.youtube.com/watch?v=1VbnNwc_ZiI', { waitUntil: 'domcontentloaded', timeout: 30000 });
    console.log('Current URL:', page.url());
    const title = await page.title();
    console.log('Title:', title);
    const description = await page.$eval('meta[name="description"]', el => el.getAttribute('content')).catch(() => 'No description');
    console.log('Description:', description);
    const html = await page.content();
    if (html.includes('Sign in to confirm')) {
      console.log('Bot detection page detected');
    }
    const match = html.match(/ytInitialPlayerResponse = (\{.+?\});/s);
    if (match) {
      const data = JSON.parse(match[1]);
      const captions = data?.captions?.playerCaptionsTracklistRenderer?.captionTracks;
      console.log('Captions:', captions ? captions.map(c => ({ lang: c.language_code, url: c.base_url })) : 'None');
    } else {
      console.log('No ytInitialPlayerResponse found');
    }
    await browser.close();
  } catch (e) {
    console.error('Error:', e.message);
  }
})();
