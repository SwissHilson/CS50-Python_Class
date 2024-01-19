'''
Extracts and returns the file extension (if any) in lower case
'''
def extract_file_extension(file_name):
    #Split the file name by dots and consider the part as the extension
    parts = file_name.split('.')
    #Return the lowercase last part as the file extention or an empty string if only one part is present
    return '.' + parts[-1].lower() if len(parts) > 1 else ''

'''
Determine the media type based on the provided file extension.
If the extension is not supported, return the default media type.
'''
def get_media_type(file_extension):
    supported_extensions = ['.gif', '.jpg', '.jpeg', '.png', '.pdf', '.txt', '.zip']

    #Map file extension to media file 
    if file_extension == '.gif':
        return 'image/gif'
    elif file_extension in ('.jpg', 'jpeg'):
        return 'image/jpeg'
    elif file_extension == '.png':
        return 'image/png'
    elif file_extension == '.pdf':
        return 'application/pdf'
    elif file_extension == '.txt':
        return 'plain/txt'
    elif file_extension == '.zip':
        return 'application/zip'
    else:
        return 'application/octet-stream'
    
    #Usage
def main():
    file = input('File name: ')
    extension = extract_file_extension(file)
    get_media = get_media_type(extension)
    print(get_media)

main()

    
