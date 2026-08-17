import os
import pygame

if not pygame.font:
   print("Warning, fonts disabled")
if not pygame.mixer:
   print("Warning, sound disabled")

main_dir = os.path.split(os.path.abspath(__file__))[0]
image_dir = os.path.join(main_dir, "../res/images")
sprite_arr = [[0 for _ in range(16)] for _ in range(16)]

def load_image(name, colorkey=None, scale=1):
   fullname = os.path.join(image_dir, name)
   image = pygame.image.load(fullname)
   image = image.convert()
   
   size = image.get_size()
   size = (size[0] * scale, size[1] * scale)
   image = pygame.transform.scale(image, size)

   if colorkey is not None:
      if colorkey == -1:
         colorkey = image.get_at((0, 0))
      image.set_colorkey(colorkey, pygame.RLEACCEL)
   return image

def create_palette(spritesheet):
   copy_rect = pygame.Rect(0, 0, 8, 16)
   colorkey = spritesheet.get_colorkey()
   for x in range(0, 16):
      for y in range(0, 16):
         sprite_arr[x][y] = pygame.Surface((8, 16))
         copy_rect.left = x * 8
         copy_rect.top = y * 16
         sprite_arr[x][y].blit(spritesheet, (0, 0), copy_rect)
         sprite_arr[x][y].set_colorkey(colorkey, pygame.RLEACCEL)

def get_colored_sprite(base_image, color):
   coloredImage = pygame.Surface(base_image.get_size())
   coloredImage.fill(color)
    
   finalImage = base_image.copy()
   finalImage.blit(coloredImage, (0, 0), special_flags = pygame.BLEND_MULT)
   return finalImage

def main():
   tick_count = 0
   fps = 0
   # Initialize Everything
   pygame.init()
   screen = pygame.display.set_mode((800, 400), pygame.SCALED)
   pygame.display.set_caption("GUI Test")
   pygame.mouse.set_visible(False)
   
   # Create The Background
   background = pygame.Surface(screen.get_size())
   background = background.convert()
   background.fill((32, 32, 32))

   # Display The Background
   screen.blit(background, (0, 0))
   pygame.display.flip()
   
   # load and portion spritesheet
   create_palette(load_image("WSFont_8x16.png", colorkey = -1))

   # Prepare Game Objects
   #allsprites = pygame.sprite.RenderPlain((chimp, fist))
   allsprites = pygame.sprite.RenderPlain(())
   clock = pygame.time.Clock()

   # Main Loop
   going = True
   while going:
      clock.tick(60)

      # Handle Input Events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            going = False
         elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            going = False

      #allsprites.update()

      # Draw Everything
      screen.blit(background, (0, 0))
      for x in range(0, 16):
         for y in range(0, 16):
            screen.blit(sprite_arr[x][y], (x * 8, y * 16))
            color_image = get_colored_sprite(sprite_arr[x][y], (255, 0, 0))
            screen.blit(color_image, ((x + 18) * 8, y * 16))
      #allsprites.draw(screen)
      tick_count += 1
      if tick_count == 30:
         tick_count = 0
         fps = clock.get_fps()
      font = pygame.font.Font(None, 32)
      text = font.render(f"FPS: {fps:.2f}", True, (255, 255, 255))
      textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
      screen.blit(text, textpos)
      
      pygame.display.flip()

   pygame.quit()

if __name__ == "__main__":
   main()
