from tkinter import *

import Classes
global Enigma


def main():
    root = Tk()
    root.title("Enigma")
    root.geometry("450x800")
    root.resizable(False, False)

    def initEnigma(reflector,
                   rotor1, rotor2, rotor3, pos1, pos2, pos3,
                   p11, p12, p21, p22, p31, p32, p41, p42, p51, p52,
                   p61, p62, p71, p72, p81, p82, p91, p92, p01, p02):
        if rotor1.get() == rotor2.get() or rotor2.get() == rotor3.get() or rotor1.get()==rotor2.get():
            EnigmaProblem_label = Label(root, text='Problem Occurred!')
            EnigmaProblem_label.place(x=173, y=470)
        else:
            r = findReflector(reflector.get())
            r1 = findRotor(rotor1.get())
            r2 = findRotor(rotor2.get())
            r3 = findRotor(rotor3.get())
            p1 = findPositioning(pos1.get())
            p2 = findPositioning(pos2.get())
            p3 = findPositioning(pos3.get())
            plugboard = [[p11.get(), p12.get()], [p21.get(), p22.get()],
                         [p31.get(), p32.get()], [p41.get(), p42.get()],
                         [p51.get(), p52.get()], [p61.get(), p62.get()],
                         [p71.get(), p72.get()], [p81.get(), p82.get()],
                         [p91.get(), p92.get()], [p01.get(), p02.get()]]
            global Enigma
            Enigma = Classes.Enigma(r, r1, r2, r3, p1, p2, p3, plugboard)
            Enigmainit_label = Label(root, text='Enigma Started Successfully!')
            Enigmainit_label.place(x=143, y=470)

    def findReflector(reflector):
        if reflector == 'Reflector B':
            return 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        if reflector == 'Reflector C':
            return 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

    def findRotor(rotor):
        if rotor == 'Rotor I':
            return 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
        if rotor == 'Rotor II':
            return 'AJDKSIRUXBLHWTMCQGZNPYFVOE'
        if rotor == 'Rotor III':
            return 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        if rotor == 'Rotor IV':
            return 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
        if rotor == 'Rotor V':
            return 'VZBRGITYUPSDNHLXAWMJQOFECK'

    def findPositioning(pos):
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for x in range(len(ALPHABET)):
            if pos == ALPHABET[x]:
                return x

    def Encrypt(letter):
        global Enigma
        pb1 = Enigma.runThroughPlugboard(letter)
        r11 = Enigma.runThroughRotorFront(pb1, 1)
        r21 = Enigma.runThroughRotorFront(r11, 2)
        r31 = Enigma.runThroughRotorFront(r21, 3)
        r = Enigma.runThroughReflector(r31)
        r32 = Enigma.runThroughRotorBack(r, 3)
        r22 = Enigma.runThroughRotorBack(r32, 2)
        r12 = Enigma.runThroughRotorBack(r22, 1)
        pb2 = Enigma.runThroughPlugboard(r12)
        Enigma.fixPositioning()

        letter_label = Label(root, text='Encrypting letter: ' + letter)
        letter_label.place(x=40, y=500)
        pb1_label = Label(root, text='Plugboard Run-through Encryption: ' + pb1)
        pb1_label.place(x=40, y=520)
        r11_label = Label(root, text='Right Rotor Run-through Encryption: ' + r11)
        r11_label.place(x=40, y=540)
        r21_label = Label(root, text='Middle Rotor Run-through Encryption: ' + r21)
        r21_label.place(x=40, y=560)
        r31_label = Label(root, text='Left Rotor Run-through Encryption: ' + r31)
        r31_label.place(x=40, y=580)
        r_label = Label(root, text='Reflector Run-through Encryption: ' + r)
        r_label.place(x=40, y=600)
        r32_label = Label(root, text='Left Rotor Run-through Encryption: ' + r32)
        r32_label.place(x=40, y=620)
        r22_label = Label(root, text='Middle Rotor Run-through Encryption: ' + r22)
        r22_label.place(x=40, y=640)
        r12_label = Label(root, text='Right Rotor Run-through Encryption: ' + r12)
        r12_label.place(x=40, y=660)
        pb2_label = Label(root, text='Plugboard Run-through Encryption: ' + pb2)
        pb2_label.place(x=40, y=680)
        final_label = Label(root, text='Encryption: \''+ letter + '\' --> \'' + pb2 + '\'')
        final_label.place(x=40, y=700)

    Enigma_label = Label(root, text='Enigma')
    Enigma_label.place(x=198, y=10)
    rotors = [
        'Rotor I',
        'Rotor II',
        'Rotor III',
        'Rotor IV',
        'Rotor V'
    ]
    reflectors = [
        'Reflector B',
        'Reflector C'
    ]
    positioning = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                   "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    first = StringVar()
    first.set(rotors[0])
    second = StringVar()
    second.set(rotors[1])
    third = StringVar()
    third.set(rotors[2])
    refl = StringVar()
    refl.set(reflectors[0])
    position1 = StringVar()
    position1.set(positioning[0])
    position2 = StringVar()
    position2.set(positioning[0])
    position3 = StringVar()
    position3.set(positioning[0])

    Reflector_label = Label(root, text='Reflector:')
    Reflector_label.place(x=25, y=45)
    Rotor1_label = Label(root, text='Rotor A:')
    Rotor1_label.place(x=150, y=45)
    Rotor2_label = Label(root, text='Rotor B:')
    Rotor2_label.place(x=250, y=45)
    Rotor3_label = Label(root, text='Rotor C:')
    Rotor3_label.place(x=350, y=45)
    Positioning_label = Label(root, text="Positioning: ")
    Positioning_label.place(x=25, y=105)
    rotor1 = OptionMenu(root, first, *rotors)
    rotor1.pack()
    rotor1.place(x=150, y=75)
    rotor2 = OptionMenu(root, second, *rotors)
    rotor2.pack()
    rotor2.place(x=250, y=75)
    rotor3 = OptionMenu(root, third, *rotors)
    rotor3.pack()
    rotor3.place(x=350, y=75)
    reflector = OptionMenu(root, refl, *reflectors)
    reflector.pack()
    reflector.place(x=25, y=75)
    positionRotor1 = OptionMenu(root, position1, *positioning)
    positionRotor1.pack()
    positionRotor1.place(x=150, y=105)
    positionRotor2 = OptionMenu(root, position2, *positioning)
    positionRotor2.pack()
    positionRotor2.place(x=250, y=105)
    positionRotor3 = OptionMenu(root, position3, *positioning)
    positionRotor3.pack()
    positionRotor3.place(x=350, y=105)

    Keyboard_label = Label(root, text='Keyboard:')
    Keyboard_label.place(x=25, y=250)

    ButtonQ = Button(root, text='Q', padx=10, pady=10, command=lambda: Encrypt('Q'))
    ButtonQ.pack()
    ButtonQ.place(x=25, y=275)
    ButtonW = Button(root, text='W', padx=10, pady=10, command=lambda: Encrypt('W'))
    ButtonW.pack()
    ButtonW.place(x=65, y=275)
    ButtonE = Button(root, text='E', padx=10, pady=10, command=lambda: Encrypt('E'))
    ButtonE.pack()
    ButtonE.place(x=108, y=275)
    ButtonR = Button(root, text='R', padx=10, pady=10, command=lambda: Encrypt('R'))
    ButtonR.pack()
    ButtonR.place(x=148, y=275)
    ButtonT = Button(root, text='T', padx=10, pady=10, command=lambda: Encrypt('T'))
    ButtonT.pack()
    ButtonT.place(x=188, y=275)
    ButtonY = Button(root, text='Y', padx=10, pady=10, command=lambda: Encrypt('Y'))
    ButtonY.pack()
    ButtonY.place(x=228, y=275)
    ButtonU = Button(root, text='U', padx=10, pady=10, command=lambda: Encrypt('U'))
    ButtonU.pack()
    ButtonU.place(x=268, y=275)
    ButtonI = Button(root, text='I', padx=12, pady=10, command=lambda: Encrypt('I'))
    ButtonI.pack()
    ButtonI.place(x=308, y=275)
    ButtonO = Button(root, text='O', padx=10, pady=10, command=lambda: Encrypt('O'))
    ButtonO.pack()
    ButtonO.place(x=348, y=275)
    ButtonP = Button(root, text='P', padx=10, pady=10, command=lambda: Encrypt('P'))
    ButtonP.pack()
    ButtonP.place(x=388, y=275)

    ButtonA = Button(root, text='A', padx=10, pady=10, command=lambda: Encrypt('A'))
    ButtonA.pack()
    ButtonA.place(x=35, y=325)
    ButtonS = Button(root, text='S', padx=10, pady=10, command=lambda: Encrypt('S'))
    ButtonS.pack()
    ButtonS.place(x=75, y=325)
    ButtonD = Button(root, text='D', padx=10, pady=10, command=lambda: Encrypt('D'))
    ButtonD.pack()
    ButtonD.place(x=115, y=325)
    ButtonF = Button(root, text='F', padx=10, pady=10, command=lambda: Encrypt('F'))
    ButtonF.pack()
    ButtonF.place(x=155, y=325)
    ButtonG = Button(root, text='G', padx=10, pady=10, command=lambda: Encrypt('G'))
    ButtonG.pack()
    ButtonG.place(x=195, y=325)
    ButtonH = Button(root, text='H', padx=10, pady=10, command=lambda: Encrypt('H'))
    ButtonH.pack()
    ButtonH.place(x=235, y=325)
    ButtonJ = Button(root, text='J', padx=10, pady=10, command=lambda: Encrypt('J'))
    ButtonJ.pack()
    ButtonJ.place(x=275, y=325)
    ButtonK = Button(root, text='K', padx=10, pady=10, command=lambda: Encrypt('K'))
    ButtonK.pack()
    ButtonK.place(x=315, y=325)
    ButtonL = Button(root, text='L', padx=10, pady=10, command=lambda: Encrypt('L'))
    ButtonL.pack()
    ButtonL.place(x=355, y=325)

    ButtonZ = Button(root, text='Z', padx=10, pady=10, command=lambda: Encrypt('Z'))
    ButtonZ.pack()
    ButtonZ.place(x=50, y=375)
    ButtonX = Button(root, text='X', padx=10, pady=10, command=lambda: Encrypt('X'))
    ButtonX.pack()
    ButtonX.place(x=90, y=375)
    ButtonC = Button(root, text='C', padx=10, pady=10, command=lambda: Encrypt('C'))
    ButtonC.pack()
    ButtonC.place(x=130, y=375)
    ButtonV = Button(root, text='V', padx=10, pady=10, command=lambda: Encrypt('V'))
    ButtonV.pack()
    ButtonV.place(x=170, y=375)
    ButtonB = Button(root, text='B', padx=10, pady=10, command=lambda: Encrypt('B'))
    ButtonB.pack()
    ButtonB.place(x=210, y=375)
    ButtonN = Button(root, text='N', padx=10, pady=10, command=lambda: Encrypt('N'))
    ButtonN.pack()
    ButtonN.place(x=250, y=375)
    ButtonM = Button(root, text='M', padx=10, pady=10, command=lambda: Encrypt('M'))
    ButtonM.pack()
    ButtonM.place(x=290, y=375)

    Plugboard_label = Label(root, text='Plugboard:')
    Plugboard_label.place(x=25, y=177)
    p11 = StringVar()
    p12 = StringVar()
    p21 = StringVar()
    p22 = StringVar()
    p31 = StringVar()
    p32 = StringVar()
    p41 = StringVar()
    p42 = StringVar()
    p51 = StringVar()
    p52 = StringVar()
    p61 = StringVar()
    p62 = StringVar()
    p71 = StringVar()
    p72 = StringVar()
    p81 = StringVar()
    p82 = StringVar()
    p91 = StringVar()
    p92 = StringVar()
    p01 = StringVar()
    p02 = StringVar()
    Pb1_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p11)
    Pb1_1.pack()
    Pb1_1.place(x=120, y=175)
    Pb1_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p12)
    Pb1_2.pack()
    Pb1_2.place(x=120, y=215)
    Pb2_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p21)
    Pb2_1.pack()
    Pb2_1.place(x=150, y=175)
    Pb2_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p22)
    Pb2_2.pack()
    Pb2_2.place(x=150, y=215)
    Pb3_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p31)
    Pb3_1.pack()
    Pb3_1.place(x=180, y=175)
    Pb3_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p32)
    Pb3_2.pack()
    Pb3_2.place(x=180, y=215)
    Pb4_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p41)
    Pb4_1.pack()
    Pb4_1.place(x=210, y=175)
    Pb4_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p42)
    Pb4_2.pack()
    Pb4_2.place(x=210, y=215)
    Pb5_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p51)
    Pb5_1.pack()
    Pb5_1.place(x=240, y=175)
    Pb5_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p52)
    Pb5_2.pack()
    Pb5_2.place(x=240, y=215)
    Pb6_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p61)
    Pb6_1.pack()
    Pb6_1.place(x=270, y=175)
    Pb6_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p62)
    Pb6_2.pack()
    Pb6_2.place(x=270, y=215)
    Pb7_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p71)
    Pb7_1.pack()
    Pb7_1.place(x=300, y=175)
    Pb7_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p72)
    Pb7_2.pack()
    Pb7_2.place(x=300, y=215)
    Pb8_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p81)
    Pb8_1.pack()
    Pb8_1.place(x=330, y=175)
    Pb8_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p82)
    Pb8_2.pack()
    Pb8_2.place(x=330, y=215)
    Pb9_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p91)
    Pb9_1.pack()
    Pb9_1.place(x=360, y=175)
    Pb9_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p92)
    Pb9_2.pack()
    Pb9_2.place(x=360, y=215)
    Pb0_1 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p01)
    Pb0_1.pack()
    Pb0_1.place(x=390, y=175)
    Pb0_2 = Entry(root, relief=GROOVE, width=2, borderwidth=2, textvariable=p02)
    Pb0_2.pack()
    Pb0_2.place(x=390, y=215)

    RunEnigma = Button(root, text='Start Enigma', padx=150, pady=10,
                       command=lambda: initEnigma(refl,
                                                  first, second, third,
                                                  position1, position2, position3,
                                                  p11, p12, p21, p22, p31, p32, p41, p42, p51, p52,
                                                  p61, p62, p71, p72, p81, p82, p91, p92, p01, p02))
    RunEnigma.pack()
    RunEnigma.place(x=35, y=430)

    root.mainloop()


main()
