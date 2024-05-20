from PIL import Image
import os

def list_files(directory):
    #List all files in the given directory.
    files = []
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            files.append(file)
    return files

def asciiConverter(scale_factor, output_file="ascii_art.txt"):
    directory = "C:\\Users\\ali\\Downloads\\asciiConverter"
    files = list_files(directory)
    
    if not files:
        print("No image files found in the directory.")
        return
    
    print("Available image files:")
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")
    
    try:
        file_choice = int(input("Enter the number corresponding to the image you want to convert: ")) - 1
        if file_choice < 0 or file_choice >= len(files):
            print("Invalid choice.")
            return
        
        input_image = files[file_choice]
        downloads_path = os.path.join(directory, input_image) # Path to the image 
        
        with Image.open(downloads_path) as img: # Open image
            # Get width and height of the selected image
            new_width = int(img.width * scale_factor)
            new_height = int(img.height * scale_factor)
            
            # Resize the image to fit the scale (needed for clear and visual output)
            img = img.resize((new_width, new_height))
            
            # Initialize grid 
            grid = [[" "] * new_width for _ in range(new_height)]
            
            # Load pixel data from inputted image
            pixel_array = img.load()
            
            # Define thresholds and corresponding ascii characters
            thresholds = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]
            ascii_chars = ["@", "#", "+", "=", ":", ".", ">", ",", ";", "-", "*", "%", "Y", "X", "&", "8", "o", "^", "`", " "]

            # Iterate over all pixels and check the brightness level 
            for h in range(new_height):
                for w in range(new_width):
                    pixel_sum = sum(pixel_array[w, h])
                    # Find the corresponding ascii character based on the thresholds
                    for threshold, char in zip(thresholds, ascii_chars): # zip function here combines two or more variables into tuples
                        if pixel_sum < threshold:
                            grid[h][w] = char
                            break
                    else:
                        grid[h][w] = ascii_chars[-1]  # Lightest pixel
            
            # Ask the user for the output method
            output_choice = input("Do you want to output the ascii art to the command line? (Y/N): ").lower()
            
            if output_choice == 'y':
                # Output to command line
                print("The image is being processed...")
                for row in grid:
                    print("".join(row))
            else:
                # Output to file
                with open(output_file, "w") as f:
                    for row in grid:
                        f.write("".join(row) + "\n")
                print("The image is being processed...")
                print("ascii art saved to", output_file)
    #Exceptions:
    except ValueError:
        print("Invalid input. Please enter a number.")

    except Exception as e:
        print("Error occurred while processing the image:", str(e))

if __name__ == "__main__":
    asciiConverter(scale_factor=0.2) # Scale can be changeable depending on image size
