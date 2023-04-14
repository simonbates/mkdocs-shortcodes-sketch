import re

shortcodes = {}

def add_shortcode(name, handler):
    shortcodes[name] = handler

def on_page_markdown(markdown, **kwargs):
    result_lines = []
    input_lines = iter(markdown.splitlines())
    for line in input_lines:
        match = re.match(r'=begin\s+(\w+)', line)
        if match:
            shortcode_name = match.group(1)
            content_lines = []
            content_line = next(input_lines)
            while not content_line.startswith('=end'):
                content_lines.append(content_line)
                content_line = next(input_lines)
            if shortcode_name in shortcodes:
                result_lines.append(shortcodes[shortcode_name]('\n'.join(content_lines)))
        else:
            result_lines.append(line)
    return '\n'.join(result_lines)

# Add shortcodes

add_shortcode('note', lambda content : '<div class="note">\n' + content + '\n</div>')
