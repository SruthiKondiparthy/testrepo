def decode1(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
 
    pairs = []
 
    for line in lines:
        parts = line.strip().split(' ')
        pairs.append((int(parts[0]), ' '.join(parts[1:])))
 
    pairs.sort()
    decoded_words = [word for _, word in pairs]
    decoded_message = ' '.join(decoded_words)
 
    return decoded_message

def decode2(message_file):
    message_dict = {}
 
    with open(message_file, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            if len(parts) == 2:
                number, word = int(parts[0]), parts[1]
                message_dict[number] = word
 
    decoded_message = [message_dict[i] for i in range(1, max(message_dict) + 1) if i in message_dict]
    return ' '.join(decoded_message)

def decode(encoded_file):
    # Read encoded message pairs of the file
    with open(encoded_file, 'r') as file:
        messages = file.readlines()
 
    # Create a dictionary to store the message pairs
    pyramid_dict = {}
 
    # Iterate through messages and fill in the pyramid_dict    
    for message in messages:
        message = message.strip().split()        
        code = int(message[0])
        code_word = message[1]
        pyramid_dict[code] = code_word
 
    # Build the decoded message by retrieving messages based on the pyramid structure
    #decoded_message = ' '.join(pyramid_dict[i] for i in range(1, len(pyramid_dict) + 1))
    decoded_message = ' '.join(pyramid_dict[i] for i in sorted(pyramid_dict))
    return decoded_message


print(decode('sample.txt')== decode1('sample.txt'))