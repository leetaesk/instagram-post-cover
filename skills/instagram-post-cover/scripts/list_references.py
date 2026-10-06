#!/usr/bin/env python3
"""List original reference links without downloading or redistributing images."""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--family')
    parser.add_argument('--decision', choices=['accepted', 'rejected'], default='accepted')
    parser.add_argument('--ids', help='Comma-separated keys; overrides family and decision')
    parser.add_argument('--limit', type=int, default=12)
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    catalog = Path(__file__).resolve().parents[1] / 'references/catalog.json'
    items = json.loads(catalog.read_text(encoding='utf-8'))['items']
    if args.ids:
        lookup = {item['key']: item for item in items}
        keys = [key.strip() for key in args.ids.split(',')]
        missing = [key for key in keys if key not in lookup]
        if missing:
            parser.error('Unknown IDs: ' + ', '.join(missing))
        items = [lookup[key] for key in keys]
    else:
        items = [item for item in items if item['decision'] == args.decision and
                 (not args.family or args.family in item['families'])]
    if not items:
        parser.error('No matching references')
    for item in items[:args.limit]:
        print(f"{item['key']}\t{item['decision']}\t{item['source_url']}")


if __name__ == '__main__':
    main()
