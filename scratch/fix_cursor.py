import sys
with open('main/static/main/shared.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace cursor: none; variations
content = content.replace('cursor: none;', '')
content = content.replace('cursor: none', '')

# Replace custom cursor block
old_cursor_css = """/* Custom Cursor — single high-contrast color, visible on all backgrounds */
.custom-cursor { 
    position: fixed; 
    top: 0; 
    left: -100px; 
    width: 18px; 
    height: 24px; 
    background-color: #ffffff; 
    pointer-events: none; 
    z-index: 9999; 
    clip-path: polygon(0% 0%, 100% 50%, 40% 50%, 40% 100%, 0% 80%);
    filter: drop-shadow(0 1px 1px rgba(0,0,0,0.6)) drop-shadow(0 0 1px rgba(0,0,0,0.8));
    will-change: left, top;
}
.custom-cursor-follower { display: none; }"""

new_cursor_css = """/* Custom CSS Cursor - Instant load, perfectly visible cross-backgrounds */
body {
    cursor: url("data:image/svg+xml,%3Csvg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M3 3L10 21L12.5 14L19.5 16.5L3 3Z' fill='%23FFFFFF' stroke='%230a2c1c' stroke-width='2' stroke-linejoin='round'/%3E%3C/svg%3E"), auto !important;
}

a, button, input, textarea, select, .magnetic-btn, .filter-btn, .view-details, .nav-links a, .portfolio-item, .social-icon, .cta-button, .view-details:hover {
    cursor: url("data:image/svg+xml,%3Csvg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Ccircle cx='12' cy='12' r='9' fill='%23FFFFFF' stroke='%230a2c1c' stroke-width='2'/%3E%3Ccircle cx='12' cy='12' r='4' fill='%230a2c1c'/%3E%3C/svg%3E"), pointer !important;
}"""

if old_cursor_css in content:
    content = content.replace(old_cursor_css, new_cursor_css)
else:
    print('Error: Could not find old cursor CSS to replace.')

with open('main/static/main/shared.css', 'w', encoding='utf-8') as f:
    f.write(content)
print('Replacements done.')
