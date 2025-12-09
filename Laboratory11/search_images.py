import sys
import requests
import os
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
CX = os.getenv("CX")

def search_and_download_images(search_term):
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    
    downloaded = 0
    start_index = 1
    max_attempts = 50  # Maximum images to try before giving up
    
    while downloaded < 10 and start_index <= max_attempts:
        # Build the search URL with pagination
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CX}&q={search_term}&searchType=image&imgSize=large&start={start_index}"
        
        try:
            # Make request to API
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # Check if results exist
            if 'items' not in data:
                print(f"No more images found for '{search_term}' at index {start_index}")
                break
            
            # Process results
            for item in data['items']:
                if downloaded >= 10:
                    break
                    
                image_url = item['link']
                
                try:
                    img_response = requests.get(image_url, timeout=10)
                    img_response.raise_for_status()
                    
                    # Open image with PIL and convert to RGB
                    img = Image.open(BytesIO(img_response.content))
                    
                    # Convert to RGB if necessary (handles PNG with transparency, etc.)
                    if img.mode in ('RGBA', 'LA', 'P'):
                        # Create white background
                        background = Image.new('RGB', img.size, (255, 255, 255))
                        if img.mode == 'P':
                            img = img.convert('RGBA')
                        background.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                        img = background
                    elif img.mode != 'RGB':
                        img = img.convert('RGB')
                    
                    # Save as JPG
                    filename = f"images/{search_term}_{downloaded + 1}.jpg"
                    img.save(filename, 'JPEG', quality=95)
                    
                    downloaded += 1
                    print(f"Downloaded and converted: {filename} ({downloaded}/10)")
                    
                except Exception as e:
                    print(f"Error downloading/converting image from {image_url}: {e}")
                    continue
            
            # Move to next page (Google API returns 10 results per page)
            start_index += 10
            
        except requests.exceptions.RequestException as e:
            print(f"Error searching for '{search_term}' at index {start_index}: {e}")
            break
        except Exception as e:
            print(f"General error: {e}")
            break
    
    if downloaded < 10:
        print(f"\nWARNING: Could only download {downloaded}/10 images for '{search_term}'")
    else:
        print(f"\nSuccessfully downloaded 10 images for '{search_term}'")

def main():
    # Check arguments
    if len(sys.argv) < 2:
        print("Usage: python search_images.py <term_1> ... <term_n>")
        sys.exit(1)
    
    # Process each search term
    search_terms = sys.argv[1:]
    print(f"Searching for {len(search_terms)} term(s)...\n")
    
    for term in search_terms:
        print(f"--- Searching: {term} ---")
        search_and_download_images(term)
        print()

if __name__ == "__main__":
    main()