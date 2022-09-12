import sys
import WordCloud

if __name__ == '__main__' :
    
    if len(sys.argv) != 4:
        print('usage: ')
        print(f'{sys.argv[0]}  [options]' )
        print('     input_file_path output_file_path method_number[0: korean, 1: english]')
        sys.exit()
    
    WordCloud.wordcloud_from_text(input_file = sys.argv[1], output_file = sys.argv[2], method = int(sys.argv[3]))                    