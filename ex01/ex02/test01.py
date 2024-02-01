file_path = 'D:\\lhc\\workspace\\python\\input.txt'

try:
    # 파일 생성
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write('안녕하세요')

    # 파일 읽기
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        words_list = [line.strip() for line in lines]  # strip() 함수로 공백 제거

    python_program = [
        "# Generated Python Program",
        "def main():",
    ]

    for line_str in words_list:
        if line_str:
            python_program.append(f'    print("{line_str}")')

    python_program.append('if __name__ == "__main__":')
    python_program.append('    main()')

    output_file_path = 'D:\\lhc\\workspace\\python\\generated_program.py'
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(python_program))

    print(f"Generated Python program saved to {output_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")