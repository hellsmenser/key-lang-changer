import keyboard
import pyperclip

ru = ['й','ц','у','к','е','ё','н','г','ш','щ','з','х','ъ','ф','ы','в','а','п','р','о','л','д','ж','э','я','ч','с','м','и','т','ь','б','ю',',','?']
eng = ["q","w","e","r","t","`","y","u","i","o","p","[","]","a","s","d","f","g","h","j","k","l",";","'","z","x","c","v","b","n","m",",",".","?","&"]

def clip_get():
	return pyperclip.paste()
def clip_set(clearClip):
	pyperclip.copy(clearClip)
	print(clearClip)


while(True):
    if(keyboard.is_pressed('t')):
        clearClip = ''
        clip = clip_get()
        for a in clip:
            try:
                if(a.lower() in eng):
                    i = eng.index(a.lower())
                    if(a.isupper()):
                        clearClip+=ru[i].upper()
                    else:
                        clearClip+=ru[i]
                else:
                    i = ru.index(a.lower())
                    if(a.isupper()):
                        clearClip+=eng[i].upper()
                    else:
                        clearClip+=eng[i]
            except:
                clearClip+=a
                print(a + " Отсутствует в списках");
            
        clip_set(clearClip)
