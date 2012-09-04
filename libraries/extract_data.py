import codecs
import json
import sys


def import_data(file_path):
    with codecs.open(file_path, encoding='utf-8') as data_file:
        js_lines = []

        # Skip lines until we reach the first `<script>` block.
        for line in data_file:
            line = line.lstrip()
            if line.startswith('<script id="blueButtonData">'):
                js_lines.append(line)
                break

        # Accumulate JS lines until we reach `</script>` tag.
        for line in data_file:
            js_lines.append(line)
            if line.rstrip().endswith('</script>'):
                break

    js_text = ''.join(js_lines)

    # Extract JSON text by trimming away text outside of opening and closing
    # curly braces.
    start_index = js_text.index('{')
    end_index = js_text.rindex('}') + 1
    json_text = js_text[start_index:end_index]

    return json.loads(json_text)


def main(file_path):
    data = import_data(file_path)
    print 'Imported data:'
    print data


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: extract_data.py <file_path>'
        sys.exit()
    main(sys.argv[1])
