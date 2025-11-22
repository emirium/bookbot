from stats import print_book_report
import sys   

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  book_filepath = sys.argv[1]
  print_book_report(book_filepath)

main()