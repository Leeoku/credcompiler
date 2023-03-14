import argparse
import logging

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='A simple Hello World script')
    parser.add_argument('-n', '--name', type=str, default='World', help='The name to say hello to')
    args = parser.parse_args()
    return args
    
def main():
    """Main function"""
    args = parse_arguments()
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Started')
    
    # Print "Hello, <name>!" to the console
    print(f'Hello, {args.name}!')
    
    logging.info('Finished')

if __name__ == '__main__':
    main()