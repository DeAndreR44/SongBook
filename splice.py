from PIL import Image

# Open the images
img1 = Image.open(r"W:\PraiseHim\screenshots\nrnrjngf.png").convert("RGB")
img2 = Image.open(r"W:\PraiseHim\screenshots\2.1.png").convert("RGB")

# Make widths equal (optional but recommended)
if img1.width != img2.width:
    new_width = max(img1.width, img2.width)
    img1 = img1.resize((new_width, int(img1.height * new_width / img1.width)))
    img2 = img2.resize((new_width, int(img2.height * new_width / img2.width)))

# Calculate final dimensions
total_height = img1.height + img2.height
combined_img = Image.new("RGB", (img1.width, total_height), color=(255, 255, 255))

# Paste both images
combined_img.paste(img1, (0, 0))
combined_img.paste(img2, (0, img1.height))

# Save the combined image
combined_img.save("339_page.jpg")

print("✅ Combined image saved as 'BestillandknowiamGod.jpg'")
