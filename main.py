import argparse
import requests


def parse_arguments():
    parser = argparse.ArgumentParser(description='Make HTTP requests.')
    parser.add_argument('domain', metavar='URL', nargs='+', help='URLs to be requested')

    args = parser.parse_args()
    return args


def perform_requests(targets):
    answers = {}
    for target in targets:
        print(f'Requesting {target} ...')
        try:
            answer = requests.get(target)
            answers[target] = answer.text
        except Exception:
            print(f'Request to {target} was unsucessful')

    return answers


def save_responses(answers):
    for probed_url in answers:
        formated_domain = probed_url.split('.')[0]
        formated_domain = formated_domain.split('/')
        formated_domain = formated_domain[-1]

        output_file = open(f'outputs/{formated_domain}.txt', 'w', encoding='utf-8')
        output_file.write(answers[probed_url])
        print(f'{probed_url} response saved in {formated_domain}.txt')

        output_file.close()


def main():
    args = parse_arguments()
    targets = args.domain

    answers = perform_requests(targets)
    save_responses(answers)


# TODO: Implement headers options using dictionaries
# TODO: Implement POST requests


if __name__ == '__main__':
    main()
