#!/usr/bin/env python3
"""
Debug WordPress update page content
"""
import urllib.request
import urllib.parse
import http.cookiejar

def debug_update_page():
    site_url = "https://uc.x0.com"
    username = "uc-japan"
    password = "Tis30426810cd067d!"
    
    # Setup session
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    opener.addheaders = [('User-Agent', 'Claude-Code-Debug/1.0')]
    
    # Login
    login_url = f"{site_url}/wp-login.php"
    login_data = {
        'log': username,
        'pwd': password,
        'wp-submit': 'ログイン',
        'redirect_to': f"{site_url}/wp-admin/",
        'testcookie': '1'
    }
    
    data = urllib.parse.urlencode(login_data).encode('utf-8')
    request = urllib.request.Request(login_url, data=data)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    
    response = opener.open(request)
    
    # Access update page
    update_url = f"{site_url}/wp-admin/update-core.php"
    response = opener.open(update_url)
    page_content = response.read().decode('utf-8')
    
    # Save full page content for analysis
    with open('/home/uc/update_page_debug.html', 'w', encoding='utf-8') as f:
        f.write(page_content)
    
    print("Update page content saved to update_page_debug.html")
    
    # Look for specific update indicators
    print("\n=== Update Page Analysis ===")
    
    # Check for various update indicators
    indicators = [
        '新しいバージョンの WordPress',
        'new version of WordPress',
        '最新版の WordPress', 
        'WordPress is up to date',
        'アップデート',
        'Update',
        'upgrade',
        'version'
    ]
    
    for indicator in indicators:
        if indicator in page_content:
            print(f"✅ Found indicator: {indicator}")
            # Find context around the indicator
            start = max(0, page_content.find(indicator) - 100)
            end = min(len(page_content), page_content.find(indicator) + 200)
            context = page_content[start:end].replace('\n', ' ').replace('\t', ' ')
            print(f"   Context: ...{context}...")
        else:
            print(f"❌ Not found: {indicator}")
    
    # Check for current WordPress version in page
    import re
    version_patterns = [
        r'WordPress\s+([0-9.]+)',
        r'バージョン\s*([0-9.]+)',
        r'version\s*([0-9.]+)',
    ]
    
    print("\n=== Version Information ===")
    for pattern in version_patterns:
        matches = re.findall(pattern, page_content, re.IGNORECASE)
        if matches:
            print(f"✅ Found versions with pattern '{pattern}': {matches}")

if __name__ == "__main__":
    debug_update_page()