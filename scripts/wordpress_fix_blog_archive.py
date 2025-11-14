#!/usr/bin/env python3
"""
WordPress Blog Archive Fixer
Fix the "View All Posts" link and create proper blog archive functionality
"""
import urllib.request
import json

class WordPressBlogArchiveFixer:
    def __init__(self):
        # Load authentication info
        try:
            with open('/home/uc/wordpress_auth.json', 'r') as f:
                self.auth_info = json.load(f)
        except FileNotFoundError:
            print("❌ Authentication info not found")
            return
        
        self.site_url = self.auth_info['site_url']
        self.token = self.auth_info['base64_token']
        self.homepage_id = 11  # From previous creation
    
    def check_current_pages(self):
        """Check existing pages on the site"""
        try:
            print("📋 Checking existing pages...")
            
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages")
            request.add_header('Authorization', f'Basic {self.token}')
            
            with urllib.request.urlopen(request) as response:
                pages = json.loads(response.read().decode('utf-8'))
            
            print(f"Found {len(pages)} pages:")
            for page in pages:
                print(f"  - {page['title']['rendered']} -> {page['link']} (ID: {page['id']})")
            
            return pages
            
        except Exception as e:
            print(f"❌ Error checking pages: {e}")
            return []
    
    def create_blog_page(self):
        """Create a proper blog archive page"""
        try:
            print("📝 Creating blog archive page...")
            
            blog_content = '''<!-- wp:heading {"textAlign":"center","level":1,"style":{"typography":{"fontSize":"2.5rem","fontWeight":"700"}}} -->
<h1 class="wp-block-heading has-text-align-center" style="font-size:2.5rem;font-weight:700">📝 UC's Blog</h1>
<!-- /wp:heading -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1.2rem"},"spacing":{"margin":{"bottom":"40px"}}}} -->
<p class="has-text-align-center" style="font-size:1.2rem;margin-bottom:40px">Welcome to my personal blog! Here you'll find stories about my adventures, temple experiences, community farming, and life in beautiful Yamanashi, Japan.</p>
<!-- /wp:paragraph -->

<!-- wp:separator {"style":{"spacing":{"margin":{"top":"20px","bottom":"40px"}}}} -->
<hr class="wp-block-separator has-alpha-channel-opacity" style="margin-top:20px;margin-bottom:40px"/>
<!-- /wp:separator -->

<!-- wp:query {"queryId":1,"query":{"perPage":"10","pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","author":"","search":"","exclude":[],"sticky":"","inherit":false},"displayLayout":{"type":"list"},"layout":{"type":"default"}} -->
<div class="wp-block-query">
<!-- wp:post-template -->
<!-- wp:group {"style":{"spacing":{"padding":{"top":"30px","bottom":"30px","left":"0px","right":"0px"},"margin":{"bottom":"40px"}},"border":{"bottom":{"color":"#e0e0e0","width":"1px"}}},"layout":{"type":"default"}} -->
<div class="wp-block-group" style="border-bottom-color:#e0e0e0;border-bottom-width:1px;margin-bottom:40px;padding-top:30px;padding-right:0px;padding-bottom:30px;padding-left:0px">
<!-- wp:post-featured-image {"isLink":true,"width":"100%","height":"300px","style":{"spacing":{"margin":{"bottom":"20px"}}}} -->
<!-- /wp:post-featured-image -->

<!-- wp:post-title {"isLink":true,"style":{"typography":{"fontSize":"1.8rem","fontWeight":"600"},"spacing":{"margin":{"bottom":"10px"}}}} -->
<!-- /wp:post-title -->

<!-- wp:group {"style":{"spacing":{"margin":{"bottom":"15px"}}},"layout":{"type":"flex","flexWrap":"nowrap"}} -->
<div class="wp-block-group" style="margin-bottom:15px">
<!-- wp:post-date {"style":{"typography":{"fontSize":"0.9rem"},"color":{"text":"#666666"}}} -->
<!-- /wp:post-date -->

<!-- wp:paragraph {"style":{"typography":{"fontSize":"0.9rem"},"color":{"text":"#666666"}}} -->
<p style="color:#666666;font-size:0.9rem"> • </p>
<!-- /wp:paragraph -->

<!-- wp:post-terms {"term":"category","style":{"typography":{"fontSize":"0.9rem"},"color":{"text":"#666666"}}} -->
<!-- /wp:post-terms -->
</div>
<!-- /wp:group -->

<!-- wp:post-excerpt {"excerptLength":30,"style":{"typography":{"fontSize":"1rem","lineHeight":"1.6"}}} -->
<!-- /wp:post-excerpt -->

<!-- wp:read-more {"content":"Continue Reading →","style":{"typography":{"fontSize":"0.9rem","fontWeight":"600"},"color":{"text":"#2c3e50"}}} -->
<!-- /wp:read-more -->
</div>
<!-- /wp:group -->
<!-- /wp:post-template -->

<!-- wp:query-pagination {"paginationArrow":"arrow","layout":{"type":"flex","justifyContent":"center"}} -->
<!-- wp:query-pagination-previous -->
<!-- /wp:query-pagination-previous -->

<!-- wp:query-pagination-numbers -->
<!-- /wp:query-pagination-numbers -->

<!-- wp:query-pagination-next -->
<!-- /wp:query-pagination-next -->
<!-- /wp:query-pagination -->

<!-- wp:query-no-results -->
<!-- wp:paragraph {"placeholder":"Add text or blocks that will display when a query returns no results."} -->
<p>No posts found yet! Stay tuned for more stories and adventures from UC!</p>
<!-- /wp:paragraph -->
<!-- /wp:query-no-results -->
</div>
<!-- /wp:query -->

<!-- wp:group {"style":{"spacing":{"padding":{"top":"40px","bottom":"20px"}},"color":{"background":"#f8f9fa"}},"layout":{"type":"default"}} -->
<div class="wp-block-group has-background" style="background-color:#f8f9fa;padding-top:40px;padding-bottom:20px">
<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"1.1rem"}}} -->
<p class="has-text-align-center" style="font-size:1.1rem">Thank you for reading! 🙏</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"typography":{"fontSize":"0.9rem"},"color":{"text":"#666666"}}} -->
<p class="has-text-align-center" style="color:#666666;font-size:0.9rem">Follow my journey of connecting hearts and minds across cultures</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph {"align":"center","style":{"spacing":{"margin":{"top":"20px"}}}} -->
<p class="has-text-align-center" style="margin-top:20px"><a href="/" class="wp-element-button">← Back to Home</a></p>
<!-- /wp:paragraph -->
</div>
<!-- /wp:group -->'''
            
            page_data = {
                "title": "Blog",
                "content": blog_content,
                "status": "publish",
                "slug": "blog"
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            blog_page_id = result['id']
            blog_url = result['link']
            
            print(f"✅ Blog archive page created!")
            print(f"📰 Blog Page ID: {blog_page_id}")
            print(f"🌐 Blog URL: {blog_url}")
            
            return result
            
        except Exception as e:
            print(f"❌ Blog page creation error: {e}")
            if hasattr(e, 'read'):
                try:
                    error_details = e.read().decode('utf-8')
                    print(f"Error details: {error_details}")
                except:
                    pass
            return None
    
    def update_homepage_blog_link(self):
        """Update the homepage to fix the blog link"""
        try:
            print("🔄 Updating homepage to fix blog link...")
            
            # Get current homepage content
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}")
            request.add_header('Authorization', f'Basic {self.token}')
            
            with urllib.request.urlopen(request) as response:
                current_page = json.loads(response.read().decode('utf-8'))
            
            # Update the content - fix the blog link
            updated_content = current_page['content']['rendered'].replace(
                '<a href="/blog" class="wp-element-button">View All Posts →</a>',
                f'<a href="{self.site_url}/blog" class="wp-element-button">View All Posts →</a>'
            )
            
            # If that doesn't work, try alternative fix
            if updated_content == current_page['content']['rendered']:
                # Use WordPress standard blog URL format
                updated_content = current_page['content']['rendered'].replace(
                    'href="/blog"',
                    f'href="{self.site_url}/blog"'
                )
            
            page_data = {
                "content": updated_content
            }
            
            data = json.dumps(page_data).encode('utf-8')
            request = urllib.request.Request(f"{self.site_url}/wp-json/wp/v2/pages/{self.homepage_id}", data=data)
            request.add_header('Authorization', f'Basic {self.token}')
            request.add_header('Content-Type', 'application/json; charset=utf-8')
            request.get_method = lambda: 'POST'
            
            with urllib.request.urlopen(request) as response:
                result = json.loads(response.read().decode('utf-8'))
            
            print("✅ Homepage blog link updated!")
            return result
            
        except Exception as e:
            print(f"❌ Homepage update error: {e}")
            return None
    
    def fix_blog_archive(self):
        """Main function to fix the blog archive functionality"""
        print("📝 Blog Archive Fixer")
        print("=" * 50)
        
        # Step 1: Check current pages
        existing_pages = self.check_current_pages()
        
        # Step 2: Check if blog page already exists
        blog_exists = any(page['slug'] == 'blog' for page in existing_pages)
        
        if not blog_exists:
            # Step 3: Create blog archive page
            blog_result = self.create_blog_page()
            
            if not blog_result:
                print("❌ Failed to create blog page")
                return False
        else:
            print("✅ Blog page already exists")
        
        # Step 4: Update homepage link
        homepage_result = self.update_homepage_blog_link()
        
        if homepage_result:
            print("\n🎉 Blog Archive Fix Completed!")
            print("=" * 60)
            print("✅ Blog archive page created/verified: DONE")
            print("✅ Homepage blog link fixed: DONE")
            print(f"🌐 Blog page: {self.site_url}/blog")
            print("\n📝 Users can now view all posts from the homepage!")
        else:
            print("❌ Failed to fix blog archive")
        
        return homepage_result

def main():
    fixer = WordPressBlogArchiveFixer()
    fixer.fix_blog_archive()

if __name__ == "__main__":
    main()