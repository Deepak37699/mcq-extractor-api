#!/usr/bin/env python3
"""
Debug table extraction
"""

def debug_table_extraction():
    test_text = """
Based on the table below, which city has the highest population?

| City | Population | Area |
|------|------------|------|
| NYC  | 8.4 million| 302  |
| LA   | 4.0 million| 469  |
| Chicago | 2.7 million| 227  |

A) New York City
B) Los Angeles
"""
    
    print("Test text:")
    print(test_text)
    print("\nLines:")
    lines = test_text.split('\n')
    for i, line in enumerate(lines):
        print(f"{i}: '{line.strip()}'")
    
    # Test table detection
    print("\nTable detection:")
    table_blocks = []
    current_table = []
    
    for i, line in enumerate(lines):
        line = line.strip()
        print(f"Line {i}: '{line}' -> has |: {('|' in line)}, count: {line.count('|')}")
        if '|' in line and line.count('|') >= 2:
            print(f"  -> Added to table")
            current_table.append(line)
        else:
            if len(current_table) >= 2:
                print(f"  -> Completed table with {len(current_table)} rows")
                table_blocks.append(current_table)
            current_table = []
    
    if len(current_table) >= 2:
        print(f"Final table with {len(current_table)} rows")
        table_blocks.append(current_table)
    
    print(f"\nFound {len(table_blocks)} table blocks")
    for i, block in enumerate(table_blocks):
        print(f"Table {i+1}:")
        for row in block:
            print(f"  {row}")

if __name__ == "__main__":
    debug_table_extraction()
