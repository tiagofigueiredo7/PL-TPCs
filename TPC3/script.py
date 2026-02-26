import re
import sys


def convert_markdown_to_html(markdown_text):
    """
    Converte Markdown parcial para HTML seguindo regras específicas:
    - Títulos: # seguido de espaço no início da linha
    - Ênfase: *texto* e **texto** (não colado a alfanuméricos)
    - Listas ordenadas e não ordenadas
    """
    lines = markdown_text.split('\n')
    result = []
    in_unordered_list = False
    in_ordered_list = False
    
    for line in lines:
        # Processar listas não ordenadas (- seguido de espaço)
        if re.match(r'^-\s+', line):
            item_text = re.sub(r'^-\s+', '', line)
            item_text = apply_emphasis(item_text)
            
            if not in_unordered_list:
                result.append('<ul>')
                in_unordered_list = True
            
            result.append(f' <li>{item_text}</li>')
            continue
        else:
            if in_unordered_list:
                result.append('</ul>')
                in_unordered_list = False
        
        # Processar listas ordenadas (N. seguido de espaço)
        if re.match(r'^\d+\.\s+', line):
            item_text = re.sub(r'^\d+\.\s+', '', line)
            item_text = apply_emphasis(item_text)
            
            if not in_ordered_list:
                result.append('<ol>')
                in_ordered_list = True
            
            result.append(f' <li>{item_text}</li>')
            continue
        else:
            if in_ordered_list:
                result.append('</ol>')
                in_ordered_list = False
        
        # Processar títulos (# no início da linha seguido de espaço)
        heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if heading_match:
            level = len(heading_match.group(1))
            title_text = heading_match.group(2)
            title_text = apply_emphasis(title_text)
            result.append(f'<h{level}>{title_text}</h{level}>')
            continue
        
        # Processar ênfase na linha normal
        line = apply_emphasis(line)
        result.append(line)
    
    # Fechar listas se ainda estiverem abertas
    if in_unordered_list:
        result.append('</ul>')
    if in_ordered_list:
        result.append('</ol>')
    
    return '\n'.join(result)


def apply_emphasis(text):
    """
    Aplica formatação de ênfase (negrito e itálico).
    - **texto** → <strong>texto</strong>
    - *texto* → <em>texto</em>
    
    Regras:
    - Não pode estar colado a caracteres alfanuméricos
    - O texto entre asteriscos não pode começar nem terminar com espaços
    """
    # Processar negrito primeiro (**texto**)
    # Usar negative lookbehind (?<!\w) e negative lookahead (?!\w)
    # para garantir que não está colado a alfanuméricos
    # \*\* - dois asteriscos literais
    # (\S(?:.*?\S)?) - texto que não começa/termina com espaço
    text = re.sub(
        r'(?<!\w)\*\*(\S(?:.*?\S)?)\*\*(?!\w)',
        r'<strong>\1</strong>',
        text
    )
    
    # Processar itálico (*texto*)
    # Similar ao negrito, mas com um asterisco
    text = re.sub(
        r'(?<!\w)\*(\S(?:.*?\S)?)\*(?!\w)',
        r'<em>\1</em>',
        text
    )
    
    return text


def main():
    if len(sys.argv) < 2:
        print("Uso: python script.py <arquivo_markdown.md>")
        print("O resultado HTML será salvo em <arquivo>.html")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = input_file.rsplit('.', 1)[0] + '.html'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = convert_markdown_to_html(markdown_content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Conversão concluída: {output_file}")
        
        # Estatísticas para as perguntas
        h1_count = html_content.count('<h1>')
        li_count = html_content.count('<li>')
        
        print(f"\nEstatísticas:")
        print(f"Tags <h1>: {h1_count}")
        print(f"Tags <li>: {li_count}")
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{input_file}' não encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
