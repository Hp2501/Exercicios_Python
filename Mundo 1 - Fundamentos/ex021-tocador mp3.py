# programa para tocar uma musica mp3

from pygame import mixer  # modulo para tocar um arquivo .mp3
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Aperte enter para fechar o programa...')
