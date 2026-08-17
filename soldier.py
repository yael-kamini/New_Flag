import consts
# paint screen one time
# pygame.display.flip()
# status = True
# while (status):
#
#   # iterate over the list of Event objects
#   # that was returned by pygame.event.get() method.
#     for i in pygame.event.get():
#
#         # if event object type is QUIT
#         # then quitting the pygame
#         # and program both.
#         if i.type == pygame.QUIT:
#             status = False
#
# # deactivates the pygame library
# pygame.quit()

pygame.draw.line(surface, (255,255,255), (x,rows_space), (x,w))
pygame.draw.line(surface, (255,255,255), (rows_space,y), (w,y))

pygame.draw.rect(surface,(0,0,200),(0,0,w,rows_space)) #top
pygame.draw.rect(surface,(0,0,200),(0,0,rows_space,w)) #left
pygame.draw.rect(surface,(0,0,200),(0,w,w + rows_space,rows_space)) #bottom
pygame.draw.rect(surface,(0,0,200),(w,0,rows_space,w + rows_space)) #right

