# debug_bedrock.py
import os
import sys
import pkgutil

def find_bedrock_modules():
    # Check the site-packages directory
    site_packages = r'C:\Users\Toffee\AppData\Local\Programs\Python\Python312\Lib\site-packages'
    print('Looking in:', site_packages)
    print()

    # Find all bedrock-related items
    bedrock_items = []
    try:
        for item in os.listdir(site_packages):
            if 'bedrock' in item.lower():
                bedrock_items.append(item)
                print(f'Found: {item}')

                # If it's a directory, show contents
                full_path = os.path.join(site_packages, item)
                if os.path.isdir(full_path):
                    try:
                        contents = os.listdir(full_path)
                        print(f'  Contents: {contents}')
                    except Exception as e:
                        print(f'  Error reading contents: {e}')
                print()
    except Exception as e:
        print(f'Error reading site-packages: {e}')

    if not bedrock_items:
        print('No bedrock-related items found in site-packages')

    # Also check if there are any .egg-info or .dist-info directories
    print('\nPackage info directories:')
    try:
        for item in os.listdir(site_packages):
            if 'bedrock' in item.lower() and ('.egg-info' in item or '.dist-info' in item):
                print(f'  {item}')
    except Exception as e:
        print(f'Error checking package info: {e}')

    # Try to find any bedrock modules using pkgutil
    print('\nSearching for bedrock modules with pkgutil...')
    found = False
    for finder, name, ispkg in pkgutil.iter_modules():
        if 'bedrock' in name.lower():
            print(f'Found module: {name} (package: {ispkg})')
            found = True

    if not found:
        print('No bedrock modules found via pkgutil')

    # Try direct imports
    print('\nTrying direct imports...')
    import_attempts = [
        'bedrock_agentcore',
        'bedrock.agentcore', 
        'bedrockagentcore',
        'bedrock_agent_core',
        'bedrock',
        'agentcore'
    ]

    for attempt in import_attempts:
        try:
            module = __import__(attempt)
            print(f'SUCCESS: {attempt}')
            print(f'  Module: {module}')
            attrs = [attr for attr in dir(module) if not attr.startswith('_')]
            print(f'  Attributes: {attrs[:10]}')  # Show first 10 attributes
        except ImportError as e:
            print(f'FAILED: {attempt} - {e}')

if __name__ == "__main__":
    find_bedrock_modules()