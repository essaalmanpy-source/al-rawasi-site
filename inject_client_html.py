import re

# The new client HTML block (same structure as existing ones)
new_client_ar = '<div class="group flex flex-col items-center gap-2 md:gap-4 shrink-0 cursor-pointer select-none"><div class="w-[120px] h-[80px] sm:w-[150px] sm:h-[100px] md:w-[280px] md:h-[180px] flex items-center justify-center p-2 md:p-4 transition-all duration-500 group-hover:-translate-y-2"><div class="relative w-full h-full"><img alt="جهاز استثمار مياه النهر الصناعي" loading="lazy" decoding="async" data-nimg="fill" class="object-contain p-1 md:p-2 transition-all duration-500 group-hover:scale-110 opacity-100" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent" src="/images/clients/man-made-river.png"/></div></div><span class="hidden md:block text-sm font-medium text-muted-foreground group-hover:text-foreground transition-colors duration-300 text-center max-w-[240px] opacity-0 group-hover:opacity-100 transform translate-y-2 group-hover:translate-y-0">جهاز استثمار مياه النهر الصناعي</span></div>'

new_client_en = '<div class="group flex flex-col items-center gap-2 md:gap-4 shrink-0 cursor-pointer select-none"><div class="w-[120px] h-[80px] sm:w-[150px] sm:h-[100px] md:w-[280px] md:h-[180px] flex items-center justify-center p-2 md:p-4 transition-all duration-500 group-hover:-translate-y-2"><div class="relative w-full h-full"><img alt="Man-Made River Water Investment Authority" loading="lazy" decoding="async" data-nimg="fill" class="object-contain p-1 md:p-2 transition-all duration-500 group-hover:scale-110 opacity-100" style="position:absolute;height:100%;width:100%;left:0;top:0;right:0;bottom:0;color:transparent" src="/images/clients/man-made-river.png"/></div></div><span class="hidden md:block text-sm font-medium text-muted-foreground group-hover:text-foreground transition-colors duration-300 text-center max-w-[240px] opacity-0 group-hover:opacity-100 transform translate-y-2 group-hover:translate-y-0">Man-Made River Water Investment Authority</span></div>'

# The marker: the last client (emaar-libya) in the scrolling section
# We need to add after each occurrence of the emaar-libya block
emaar_marker = 'src="/images/clients/emaar-libya.png"/></div></div><span class="hidden md:block text-sm font-medium text-muted-foreground group-hover:text-foreground transition-colors duration-300 text-center max-w-[240px] opacity-0 group-hover:opacity-100 transform translate-y-2 group-hover:translate-y-0">'

def add_client_to_file(filepath, new_block, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if lang == 'ar':
        emaar_name = 'شركة إعمار ليبيا القابضة'
    else:
        emaar_name = 'Emaar Libya Holding Co.'
    
    # Find the full emaar block ending and insert new client after it
    search = emaar_marker + emaar_name + '</span></div>'
    replacement = search + new_block
    
    new_content = content.replace(search, replacement)
    
    count = content.count(search)
    print(f"Found {count} occurrences of emaar block in {filepath}")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"Updated {filepath}")

# Update Arabic page
add_client_to_file(
    r'C:\Users\ALMANPY\Desktop\al-rawasi-site-main\static-site\ar\index.html',
    new_client_ar,
    'ar'
)

# Update English page
add_client_to_file(
    r'C:\Users\ALMANPY\Desktop\al-rawasi-site-main\static-site\en\index.html',
    new_client_en,
    'en'
)

print("Done!")
