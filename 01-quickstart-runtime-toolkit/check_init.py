# check_init.py
import os
import sys

def check_bedrock_init():
    site_packages = r'C:\Users\Toffee\AppData\Local\Programs\Python\Python312\Lib\site-packages'
    bedrock_path = os.path.join(site_packages, 'bedrock_agentcore')

    print(f'Checking: {bedrock_path}')
    print(f'Directory exists: {os.path.exists(bedrock_path)}')
    print(f'Is directory: {os.path.isdir(bedrock_path)}')

    init_file = os.path.join(bedrock_path, '__init__.py')
    print(f'__init__.py exists: {os.path.exists(init_file)}')

    if os.path.exists(init_file):
        print(f'__init__.py size: {os.path.getsize(init_file)} bytes')

        # Try to read the __init__.py file
        try:
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(f'__init__.py content (first 500 chars):')
                print(content[:500])
                print('...' if len(content) > 500 else '')
        except Exception as e:
            print(f'Error reading __init__.py: {e}')

    # Check if we can add the path manually
    print('\nTrying manual path addition...')
    if site_packages not in sys.path:
        sys.path.insert(0, site_packages)
        print('Added site-packages to sys.path')

    try:
        import bedrock_agentcore
        print('SUCCESS: Manual import worked!')
        print(f'Module: {bedrock_agentcore}')
        print(f'Module file: {bedrock_agentcore.__file__}')
        attrs = [attr for attr in dir(bedrock_agentcore) if not attr.startswith('_')]
        print(f'Available attributes: {attrs}')

        # Check for BedrockAgentCoreApp
        if hasattr(bedrock_agentcore, 'BedrockAgentCoreApp'):
            print('BedrockAgentCoreApp found!')
        else:
            print('BedrockAgentCoreApp NOT found in main module')
            # Check submodules
            for attr in attrs:
                try:
                    submodule = getattr(bedrock_agentcore, attr)
                    if hasattr(submodule, 'BedrockAgentCoreApp'):
                        print(f'BedrockAgentCoreApp found in {attr}!')
                except:
                    pass

    except Exception as e:
        print(f'Manual import failed: {e}')

        # Try importing submodules directly
        print('\nTrying submodule imports...')
        submodules = ['runtime', 'services', 'tools', 'identity', 'memory']
        for sub in submodules:
            try:
                module_name = f'bedrock_agentcore.{sub}'
                submodule = __import__(module_name, fromlist=[sub])
                print(f'SUCCESS: {module_name}')
                if hasattr(submodule, 'BedrockAgentCoreApp'):
                    print(f'  BedrockAgentCoreApp found in {sub}!')
            except Exception as sub_e:
                print(f'FAILED: {module_name} - {sub_e}')

if __name__ == "__main__":
    check_bedrock_init()