from reportlab.lib.colors import black     # pip install reportlab
from reportlab.lib.pagesizes import LETTER 
from reportlab.lib.units import inch,cm
from reportlab.pdfgen.canvas import Canvas as cn
from pathlib import Path
import PyPDF2                              #pip install PyPDF2

import os                               # pip install xlrd  
                                        # pip install openpyxl
import datetime                                        
import time
from tkinter import *
from tkinter.ttk import * 
from PIL import ImageTk,Image
import pandas as pds
from pandas import ExcelWriter             # pip install pandas
from pandas import ExcelFile
import numpy
import pyautogui as ptg
import webbrowser

pavatinumber_path = 'ExcelFiles//pavatinumber.xlsx'
path_measurements = 'ExcelFiles//measurements.xlsx'

input_file_print_bill = "pdfFiles//print1.pdf"
watermark_file_print_bill = "pdfFiles//watermarktaior1.pdf"

#browser_path_pdf = "file:///C:/Users/Mahesh comp/Desktop/mahalakshmi4/pdfFiles/"
browser_path_pdf = "file:///D:/Work/Softwares/mahalakshmi4/pdfFiles/"

def login():
    name=name_entry.get() 
    password=passw_entry.get() 
      
    print("The name is : " + name) 
    print("The password is : " + password) 

    if name == 'mahesh':
        if password == '6797':
            print('welcome')
            main_frame()           
        else:
            print('wrong entry')  
            login_fail.place(x = 1040,y = 150)
    else:
        print('wrong entry')  
        login_fail.place(x = 1020,y = 150)
    name_var.set("") 
    passw_var.set("")  

def main():
    my.place(x=0,y=0)
    name_label.place(x = 950,y = 50)
    name_entry.place(x = 1080,y = 50) 
    passw_label.place(x = 950,y = 100)
    passw_entry.place(x = 1080,y = 100)
    login_button.place(x = 1040, y = 180)

def main_frame():
    my.destroy()
    Login_A.destroy()
    name_label.destroy()
    passw_label.destroy()
    name_entry.destroy()
    passw_entry.destroy()
    login_fail.destroy()
    login_button.destroy()
    print('now i am in main frame')


    A = Canvas(root, bg =background1, height = 150, width = 1366,relief=FLAT) 
    A.place(x=0,y=0)
    B = Canvas(root, bg =background2, height = 570, width = 156,relief=FLAT) 
    B.place(x=0,y=150)
    c = Canvas(root, bg =background2, height = 10, width = 1216,relief=FLAT) 
    c.place(x=158,y=150)

        
    main_title3 = Label(text="mhal(mI ",font=("Marathi-Lekhani", 60, 'bold'),background=background1,foreground="red")
    main_title4 = Label(text="TOP SHOP",font=("calibri", 30, 'bold'),background=background1,foreground="red")
    main_title5 = Label(text="re.da; ",font=("Marathi-Lekhani", 32, 'bold'),background=background1,foreground="red")

    button1 = Button(root, text = "Measurement",style = 'W.TButton',command = canvas_excel_1)
    button2 = Button(root, text = "Bill",style = 'W.TButton',command = canvas_excel_2)
    button3 = Button(root, text = "About",style = 'W.TButton',command = About)


    main_title3.place(x=500,y=1)
    main_title4.place(x=620,y=90)
    main_title5.place(x=800,y=88)
    button1.place(x=20,y=170)
    button2.place(x=20,y=220)
    button3.place(x=20,y=270)

    canvas_excel_1()
    # canvas_excel_2()

def About():
    print('About')
    A = Canvas(root, bg ="white", height = 570, width = 1216,relief=FLAT) 
    A.place(x=158,y=160)
    c = Canvas(root, bg =background2, height = 10, width = 1216,relief=FLAT) 
    c.place(x=158,y=150)
    e = Canvas(root, bg =background2, height = 10, width = 1216,relief=FLAT) 
    e.place(x=158,y=430)

    header1 = Label(text="mhal(mI ",font=("Marathi-Lekhani", 32, 'bold'),background=background1,foreground="black")
    header2 = Label(text="TOP SHOP ",font=("calibri", 30, 'bold'),background=background1,foreground="black")
    header3 = Label(text="iv#\#l m.dIr jv;, re.da;|  ",font=("Marathi-Lekhani", 15),background=background1,foreground="black")
    header4 = Label(text="mo|",font=("Marathi-Lekhani", 15),background=background1,foreground="black")
    header5 = Label(text="8830272430",font=("calibri", 13),background=background1,foreground="black")

    header1.place(x=200,y=180)
    header2.place(x=350,y=182)
    header3.place(x=200,y=235)
    header4.place(x=200,y=260)
    header5.place(x=230,y=262)
    # header1 = Label(text="Mahalakshmi Top Shop",font=("Helvetica", 15),background="white",foreground="black")
    # header1 = Label(text="Near Vithhal Mandir, ",font=("Helvetica", 15),background="white",foreground="black")
    # header3 = Label(text="Software developed by,",font=("Helvetica", 15),background="white",foreground="black")
    # header4 = Label(text="Software developed by,",font=("Helvetica", 15),background="white",foreground="black")

    header6 = Label(text="Software developed by,",font=("Helvetica", 15),background="white",foreground="black")
    header7=Label(text='Er.Onkar Anil Deshpande', font = ('calibri', 25, 'bold'),background="white")
    # header8=Label(text='Electronics & Telecommunication Engineer', font = ('calibri', 15, 'italic'),background="white")
    header9=Label(text='E-mail ID : onkard543@gmail.com', font = ('calibri', 15, 'italic'),background="white")
    header10=Label(text='Phone: 9552708854', font = ('calibri', 15, 'italic'),background="white")
    header6.place(x=880,y=490)
    header7.place(x=940,y=520)
    header9.place(x=940,y=560)
    header10.place(x=940,y=590)

def print_bill():
    print("_________________print_bill_______________________________")
    sheet1 = pds.read_excel(path_pavatinumber, sheet_name = "Sheet1") 
    sheet1.set_index('index', inplace = True)
    counter1=sheet1.loc[0][0]
    pn1=counter1
    pn3 = Label(text="##########",font=("calibre", font1, 'normal'),background=background1,foreground="white")
    pn2 = Label(text=pn1,font=("calibre", font1, 'normal'),background=background1,foreground="black")
    pn3.place(x=855 ,y=172)
    pn2.place(x=855 ,y=172)
    print(pn1)


    # output_file = "pdfFiles//finalBill.pdf"
    output_file_print_bill = "pdfFiles//"+str(pn1)+".pdf"

    with open(input_file, "rb") as filehandle_input:
        # read content of the original file
        pdf = PyPDF2.PdfFileReader(filehandle_input)
        
        with open(watermark_file, "rb") as filehandle_watermark:
            # read content of the watermark
            watermark = PyPDF2.PdfFileReader(filehandle_watermark)
            
            # get first page of the original PDF
            first_page = pdf.getPage(0)
            
            # get first page of the watermark PDF
            first_page_watermark = watermark.getPage(0)
            
            # merge the two pages
            first_page.mergePage(first_page_watermark)
            
            # create a pdf writer object for the output file
            pdf_writer = PyPDF2.PdfFileWriter()
            
            # add page
            pdf_writer.addPage(first_page)
            
            with open(output_file, "wb") as filehandle_output:
                # write the watermarked file to the new file
                pdf_writer.write(filehandle_output)
    ptg.FAILSAFE=False


    browser=browser_path_pdf+str(pn1)+'.pdf'
    browser=+str(pn1)+'.pdf'
    webbrowser.open_new(browser)
    time.sleep(3)
    ptg.hotkey('ctrl','p')
    time.sleep(4)
    ptg.click(157,613)
    time.sleep(3)
    ptg.hotkey('alt','F4')
    
def print_bill1():
    
    input_file = "pdfFiles//print.pdf"
    output_file = "pdfFiles//finalBill.pdf"
    watermark_file = "pdfFiles//shopbillprint1.pdf"

    with open(input_file, "rb") as filehandle_input:
        # read content of the original file
        pdf = PyPDF2.PdfFileReader(filehandle_input)
        
        with open(watermark_file, "rb") as filehandle_watermark:
            # read content of the watermark
            watermark = PyPDF2.PdfFileReader(filehandle_watermark)
            
            # get first page of the original PDF
            first_page = pdf.getPage(0)
            
            # get first page of the watermark PDF
            first_page_watermark = watermark.getPage(0)
            
            # merge the two pages
            first_page.mergePage(first_page_watermark)
            
            # create a pdf writer object for the output file
            pdf_writer = PyPDF2.PdfFileWriter()
            
            # add page
            pdf_writer.addPage(first_page)
            
            with open(output_file, "wb") as filehandle_output:
                # write the watermarked file to the new file
                pdf_writer.write(filehandle_output)
    ptg.FAILSAFE=False
    browser="file:///C:/Users/Mahesh comp/Desktop/mahalakshmi4/pdfFiles/finalBill.pdf"
    webbrowser.open_new(browser)
    time.sleep(3)
    ptg.hotkey('ctrl','p')
    time.sleep(4)
    ptg.click(157,613)
    time.sleep(3)
    ptg.hotkey('alt','F4')

def canvas_excel_1():

    print("canvas_excel_1___________________________________________________")

    def total1():
        print("total1 ___________________________________________________")
        shirt6=int(shirt3.get())
        pant6=int(pant3.get())
        safari6=int(safari3.get())
        salvar6=int(salvar3.get())
        shirtpis6=int(shirtpis3.get())
        pantpis6=int(pantpis3.get())

        shirt5=int(shirt33.get())
        pant5=int(pant33.get())
        safari5=int(safari33.get())
        salvar5=int(salvar33.get())
        shirtpis5=int(shirtpis33.get())
        pantpis5=int(pantpis33.get())
        advance5=int(advance33.get())

        discount5=int(discount33.get())

        shirt7=shirt5*shirt6
        pant7=pant5*pant6
        safari7=safari5*safari6
        salvar7=salvar5*salvar6
        shirtpis7=shirtpis5*shirtpis6
        pantpis7=pantpis5*pantpis6
        
        # shirt333=Label(text=shirt7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        # pant333=Label(text=pant7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        # safari333=Label(text=safari7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        # salvar333=Label(text=salvar7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        # shirtpis333=Label(text=shirtpis7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        # pantpis333=Label(text=pantpis7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        
        # shirt333.place(x=1230.5,y=307)
        # pant333.place(x=1230.5,y=337)
        # safari333.place(x=1230.5,y=367)
        # salvar333.place(x=1230.5,y=397)
        # shirtpis333.place(x=1230.5,y=427)
        # pantpis333.place(x=1230.5,y=457)


        ekun33_var=shirt7 + pant7 + safari7 + salvar7 + shirtpis7 + pantpis7
        print(ekun33_var)
        print(discount5)

        total = ekun33_var - (discount5 * ekun33_var)/100
        print(total)
        ekun333= Label(text=total,font=("calibre", font, 'bold'),background=background1,foreground="black")
        ekun333.place(x=1232,y=517)

        yene5=total-advance5
        print(yene5)
        # yene33= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="black")
        yene33= Label(text=yene5,font=("calibre", font, 'bold'),background=background1,foreground="black")
        yene33.place(x=1230.5,y=577)

        print("print Button")
        button4 = Button(root, text = "Print",style = 'W.TButton',command = canvas_1)
        button4.place(x=1000,y=635)

        return shirt5,pant5,safari5,salvar5,shirtpis5,pantpis5,shirt7,pant7,safari7,salvar7,shirtpis7,pantpis7,yene5,discount5,total

    def excel_1():
        print("excel_1 ______________________________________________")
        #_________main bil__________
        shirt55,pant55,safari55,salvar55,shirtpis55,pantpis55,shirt77,pant77,safari77,salvar77,shirtpis77,pantpis77,yene55,discount55,ekun33=total1()
        advance55=int(advance33.get())
        # yene55=int(yene33.get())

        shirt5 = int(shirt3.get())
        pant5 = int(pant3.get())
        safari5 = int(safari3.get())
        salvar5 = int(salvar3.get())
        shirtpis5 = int(shirtpis3.get())
        pantpis5 = int(pantpis3.get())

        shree11 = shree1.get()
        mobile11 = int(mobile1.get())

        #_______________shirt________________
        unchi11= unchi1.get()
        sholder11= sholder1.get()
        astin11= astin1.get()
        kap11= kaP1.get()
        gala11= gala1.get()
        chati11= chati1.get()
        pot11= pot1.get()
        sit11= sit1.get()
        front11= front1.get()
        front12= front111.get()
        front13= front1111.get()
        print(unchi11,sholder11,astin11,kap11,gala11,chati11,pot11,sit11,front11,front111,front1111)


        #_______________pant_________________
        unchi22 = unchi2.get()
        kamar22 = kamar2.get()
        sit22 = sit2.get()
        mandi22 = mandi2.get()
        chain22 = chain2.get()
        gudgha22 = gudgha2.get()
        bottom22 = bottom2.get()
        print(unchi22,kamar22,sit22,mandi22,chain22,gudgha22,bottom22)


        #________________counter_________________
        sheet1 = pds.read_excel(pavatinumber_path, sheet_name = "Sheet1") 
        sheet1.set_index('index', inplace = True)
        counter1=sheet1.loc[0][0]

        pn1=counter1

        print("excel________123___________________________________________________________________________")
        sheet2 = pds.read_excel(path_measurements, sheet_name = "Sheet1") 
        my_list1 = sheet2.columns.values.tolist()

        df2=pds.DataFrame({'mobile ':[mobile11],'pavati':[pn1],'Name':[shree11],'date':[date1]
                        ,'unchi1':[unchi11],'sholder1':[sholder11],'Astin1':[astin11],'kap1':[kap11]
                        ,'gala1':[gala11],'chati1':[chati11],'pot1':[pot11],'sit1':[sit11],'front1':[front11],'front2':[front12],'front3':[front13]
                        ,'unchi2':[unchi22],'kamar2':[kamar22],'sit2':[sit22],'mandi2':[mandi22]
                        ,'chain2':[chain22],'gudaga2':[gudgha22],'botam2':[bottom22]
                        ,'shirt3':[shirt5],'pant3':[pant5],'safari3':[safari5]
                        ,'salavar3':[salvar5],'shirtpis3':[shirtpis5],'pantpis3':[pantpis5]
                        ,'shirt33':[shirt55],'pant33':[pant55],'safari33':[safari55]
                        ,'salavar33':[salvar55],'shirtpis33':[shirtpis55],'pantpis33':[pantpis55]
                        ,'shirt333':[shirt77],'pant333':[pant77],'safari333':[safari77]
                        ,'salavar333':[salvar77],'shirtpis333':[shirtpis77],'pantpis333':[pantpis77]
                        ,'discount33':[discount55],'total33':[ekun33],'advance33':[advance55],'yene33':[yene55]})
        print(df2)

        df3=sheet2.append(df2) 
        print(df3)

        df3.to_excel(path_measurements, sheet_name = "Sheet1",index = False) 
        print_bill()

    def canvas_1():
        print("canvas_1 Start")
        #_________main bil__________
        shirt55,pant55,safari55,salvar55,shirtpis55,pantpis55,shirt77,pant77,safari77,salvar77,shirtpis77,pantpis77,yene55,discount55,ekun33=total1()
        advance55=int(advance33.get())
        # yene55=int(yene33.get())
        print(shirt55,pant55,safari55,salvar55,shirtpis55,pantpis55,discount55, ekun33,yene55,advance55)

        shirt5 = int(shirt3.get())
        pant5 = int(pant3.get())
        safari5 = int(safari3.get())
        salvar5 = int(salvar3.get())
        shirtpis5 = int(shirtpis3.get())
        pantpis5 = int(pantpis3.get())
        # print(shirt5,pant5,safari5,salvar5,shirtpis5,pantpis5)

        shree11 = shree1.get()
        mobile11 = int(mobile1.get())
        print(shree11,mobile11)

        #_______________shirt________________
        unchi11= unchi1.get()
        sholder11= sholder1.get()
        astin11= astin1.get()
        kap11= kaP1.get()
        gala11= gala1.get()
        chati11= chati1.get()
        pot11= pot1.get()
        sit11= sit1.get()
        front11= front1.get()
        front12= front111.get()
        front13= front1111.get()
        print(unchi11,sholder11,astin11,kap11,gala11,chati11,pot11,sit11,front11,front111,front1111)

        #_______________pant_________________
        unchi22 = unchi2.get()
        kamar22 = kamar2.get()
        sit22 = sit2.get()
        mandi22 = mandi2.get()
        chain22 = chain2.get()
        gudgha22 = gudgha2.get()
        bottom22 = bottom2.get()
        print(unchi22,kamar22,sit22,mandi22,chain22,gudgha22,bottom22)


        #__________________canvas for values put in pdf_____________________________________
        canvas = cn("pdfFiles//print1.pdf", pagesize=LETTER)
        # Set font to Times New Roman with 12-point size
        canvas.setFont("Times-Roman", 10)

        #___________________counter____________________________________________________
        sheet1 = pds.read_excel(pavatinumber_path, sheet_name = "Sheet1") 
        sheet1.set_index('index', inplace = True)
        counter1=sheet1.loc[0][0]
        counter1+=1
        print(counter1) 
        sheet1.loc[0][0]= counter1
        sheet1.to_excel(pavatinumber_path, sheet_name = "Sheet1")
        pn1=counter1

        pn3 = Label(text="##########",font=("calibre", font1, 'normal'),background=background1,foreground="white")
        pn2 = Label(text=pn1,font=("calibre", font1, 'normal'),background=background1,foreground="black")
        pn3.place(x=855 ,y=172)
        pn2.place(x=855 ,y=172)
        print("-----------------------------------------------------------------")
        print(pn1)

    
        #___________________shirt__________________
        # Draw blue text one inch from the left and ten # inches from the bottom

        canvas.drawString(2 * cm, 25.4 * cm, str(pn1)) 
        canvas.drawString(2 * cm, 24.9 * cm, str(shree11)) 
        canvas.drawString(2 * cm, 24.3 * cm, str(mobile11)) 
        canvas.drawString(6.5 * cm, 24.3 * cm, str(date1)) 
        canvas.drawString(2.2 * cm, 23.1 * cm, str(unchi11)) 
        canvas.drawString(3.7 * cm, 23.1 * cm, str(sholder11)) 
        canvas.drawString(5.3 * cm, 23.1 * cm, str(astin11)) 
        canvas.drawString(6.9 * cm, 23.1 * cm, str(kap11)) 
        canvas.drawString(2.2 * cm, 21.9 * cm, str(gala11)) 
        canvas.drawString(3.7 * cm, 21.9 * cm, str(chati11)) 
        canvas.drawString(5.3 * cm, 21.9 * cm, str(pot11)) 
        canvas.drawString(6.9 * cm, 21.9 * cm, str(sit11)) 
        canvas.drawString(2.2 * cm, 20.7 * cm, str(front11)) 
        canvas.drawString(2.2 * cm, 20.2 * cm, str(front12)) 
        canvas.drawString(2.2 * cm, 19.6 * cm, str(front13))
        canvas.drawString(2.2 * cm, 19.1 * cm, str(shirtDiscription1111.get()))
 
        #____________________pant______________________________

        canvas.drawString(2 * cm, 17.4 * cm, str(pn1)) 
        canvas.drawString(6.5 * cm, 17.4 * cm, str(date1))
        canvas.drawString(2.2 * cm, 16.2 * cm, str(unchi22)) 
        canvas.drawString(3.7 * cm, 16.2 * cm, str(kamar22)) 
        canvas.drawString(5.3 * cm, 16.2 * cm, str(sit22)) 
        canvas.drawString(6.9 * cm, 16.2 * cm, str(mandi22)) 
        canvas.drawString(2.2 * cm, 15 * cm, str(chain22)) 
        canvas.drawString(3.7 * cm, 15 * cm, str(gudgha22)) 
        canvas.drawString(5.3 * cm, 15 * cm, str(bottom22)) 
        canvas.drawString(2.2 * cm, 14.5 * cm, str(pantDiscription1111.get()))

        #_______________main bill______________________________

        canvas.drawString(11.2 * cm, 24.3 * cm, str(pn1)) 
        canvas.drawString(11.2 * cm, 23.7 * cm, str(shree11)) 
        canvas.drawString(11.2* cm, 23.1 * cm, str(mobile11)) 
        canvas.drawString(16 * cm, 23.1 * cm, str(date1))

        canvas.drawString(16 * cm, 21.3 * cm, str(shirt5))
        canvas.drawString(16 * cm, 20.7 * cm, str(pant5))
        canvas.drawString(16 * cm, 20.1 * cm, str(safari5))
        canvas.drawString(16 * cm, 19.6 * cm, str(salvar5))
        canvas.drawString(16 * cm, 19 * cm, str(shirtpis5))
        canvas.drawString(16 * cm, 18.5 * cm, str(pantpis5))

        canvas.drawString(17 * cm, 21.3 * cm, str(shirt55))
        canvas.drawString(17 * cm, 20.7 * cm, str(pant55))
        canvas.drawString(17 * cm, 20.1 * cm, str(safari55))
        canvas.drawString(17 * cm, 19.6 * cm, str(salvar55))
        canvas.drawString(17 * cm, 19 * cm, str(shirtpis55))
        canvas.drawString(17 * cm, 18.5 * cm, str(pantpis55))

        canvas.drawString(18.3 * cm, 21.3 * cm, str(shirt77))
        canvas.drawString(18.3 * cm, 20.7 * cm, str(pant77))
        canvas.drawString(18.3 * cm, 20.1 * cm, str(safari77))
        canvas.drawString(18.3 * cm, 19.6 * cm, str(salvar77))
        canvas.drawString(18.3 * cm, 19 * cm, str(shirtpis77))
        canvas.drawString(18.3 * cm, 18.5 * cm, str(pantpis77))

        canvas.drawString(18.3 * cm, 17.9 * cm, str(discount55))
        canvas.drawString(18.3 * cm, 17.4 * cm, str(ekun33))
        canvas.drawString(18.3 * cm, 16.8 * cm, str(advance55))
        canvas.drawString(18.3 * cm, 16.2 * cm, str(yene55))


        # canvas.drawString(72, 72, "Hello, World")
        # Save the PDF file
        canvas.save()
        print("done")

        # print_bill()
        excel_1()
        #_____________________________________________________________________________________________________________
 
    def search1():
        
        def total3():
            shirt6=int(shirt3.get())
            pant6=int(pant3.get())
            safari6=int(safari3.get())
            salvar6=int(salvar3.get())
            shirtpis6=int(shirtpis3.get())
            pantpis6=int(pantpis3.get())

            shirt5=int(shirt33.get())
            pant5=int(pant33.get())
            safari5=int(safari33.get())
            salvar5=int(salvar33.get())
            shirtpis5=int(shirtpis33.get())
            pantpis5=int(pantpis33.get())
            advance5=int(advance33.get())

            discount5=int(discount33.get())

            shirt7=shirt5*shirt6
            pant7=pant5*pant6
            safari7=safari5*safari6
            salvar7=salvar5*salvar6
            shirtpis7=shirtpis5*shirtpis6
            pantpis7=pantpis5*pantpis6
            
            shirt333=Label(text=shirt7,font=("calibre", font, 'bold'),background=background1,foreground="black")
            pant333=Label(text=pant7,font=("calibre", font, 'bold'),background=background1,foreground="black")
            safari333=Label(text=safari7,font=("calibre", font, 'bold'),background=background1,foreground="black")
            salvar333=Label(text=salvar7,font=("calibre", font, 'bold'),background=background1,foreground="black")
            shirtpis333=Label(text=shirtpis7,font=("calibre", font, 'bold'),background=background1,foreground="black")
            pantpis333=Label(text=pantpis7,font=("calibre", font, 'bold'),background=background1,foreground="black")
            
            shirt333.place(x=1230.5,y=307)
            pant333.place(x=1230.5,y=337)
            safari333.place(x=1230.5,y=367)
            salvar333.place(x=1230.5,y=397)
            shirtpis333.place(x=1230.5,y=427)
            pantpis333.place(x=1230.5,y=457)


            ekun33_var=shirt7 + pant7 + safari7 + salvar7 + shirtpis7 + pantpis7
            print(ekun33_var)
            print(discount5)

            total = ekun33_var - (discount5 * ekun33_var)/100
            print(total)
            ekun333= Label(text=total,font=("calibre", font, 'bold'),background=background1,foreground="black")
            ekun333.place(x=1232,y=517)

            yene5=total-advance5
            print(yene5)
            # yene33= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="black")
            yene33= Label(text=yene5,font=("calibre", font, 'bold'),background=background1,foreground="black")
            yene33.place(x=1230.5,y=577)

            button4 = Button(root, text = "Print",style = 'W.TButton',command = canvas_3)
            button4.place(x=1000,y=635)

            return shirt5,pant5,safari5,salvar5,shirtpis5,pantpis5,shirt7,pant7,safari7,salvar7,shirtpis7,pantpis7,advance5,yene5,discount5,total

        def excel_3():
            print("excel")
            #_________main bil__________
            shirt55,pant55,safari55,salvar55,shirtpis55,pantpis55,shirt77,pant77,safari77,salvar77,shirtpis77,pantpis77,advance55,yene55,discount55,ekun33 =total3()
            # advance55=int(advance33.get())
            # yene55=int(yene33.get())

            shirt5 = int(shirt3.get())
            pant5 = int(pant3.get())
            safari5 = int(safari3.get())
            salvar5 = int(salvar3.get())
            shirtpis5 = int(shirtpis3.get())
            pantpis5 = int(pantpis3.get())

            shree11 = shree1.get()
            mobile11 = int(mobile1.get())

            #_______________shirt________________
            unchi11= unchi4.get()
            sholder11= sholder4.get()
            astin11= astin4.get()
            kap11= kaP4.get()
            gala11= gala4.get()
            chati11= chati4.get()
            pot11= pot4.get()
            sit11= sit4.get()
            front11= front4.get()
            front12= front444.get()
            front13= front4444.get()
            print(unchi11,sholder11,astin11,kap11,gala11,chati11,pot11,sit11,front11,front12,front13)
            print('::::')

            #_______________pant_________________
            unchi22 = unchi5.get()
            kamar22 = kamar5.get()
            sit22 = sit5.get()
            mandi22 = mandi5.get()
            chain22 = chain5.get()
            gudgha22 = gudgha5.get()
            bottom22 = bottom5.get()
            print(unchi22,kamar22,sit22,mandi22,chain22,gudgha22,bottom22)



            #________________counter_________________
            sheet1 = pds.read_excel(pavatinumber_path, sheet_name = "Sheet1") 
            sheet1.set_index('index', inplace = True)
            counter1=sheet1.loc[0][0]
            pn1=counter1

            print("excel")

            sheet2 = pds.read_excel(path_measurements, sheet_name = "Sheet1") 
            sheet2.set_index('mobile ', inplace = True)

            mobile12=int(mobile1.get())
            print(mobile12)
            # my_list1 = sheet2.columns.values.tolist()
            # df2=pds.DataFrame({'mobile ':[mobile11],'pavati':[pn1],'Name':[shree11],'date':[date1]
            #                 ,'unchi1':[unchi11],'sholder1':[sholder11],'Astin1':[astin11],'kap1':[kap11]
            #                 ,'gala1':[gala11],'chati1':[chati11],'pot1':[pot11],'sit1':[sit11],'front1':[front11],'front2':[front12],'front3':[front13]
            #                 ,'unchi2':[unchi22],'kamar2':[kamar22],'sit2':[sit22],'mandi2':[mandi22]
            #                 ,'chain2':[chain22],'gudaga2':[gudgha22],'botam2':[bottom22]
            #                 ,'shirt3':[shirt5],'pant3':[pant5],'safari3':[safari5]
            #                 ,'salavar3':[salvar5],'shirtpis3':[shirtpis5],'pantpis3':[pantpis5]
            #                 ,'shirt33':[shirt55],'pant33':[pant55],'safari33':[safari55]
            #                 ,'salavar33':[salvar55],'shirtpis33':[shirtpis55],'pantpis33':[pantpis55]
            #                 ,'shirt333':[shirt77],'pant333':[pant77],'safari333':[safari77]
            #                 ,'salavar333':[salvar77],'shirtpis333':[shirtpis77],'pantpis333':[pantpis77]
            #                 ,'discount33':[discount55],'total33':[ekun33],'advance33':[advance55],'yene33':[yene55]})
            # print(df2)
            # df3=sheet2.append(df2) 
            # print(df3)

                
            # # pavati=sheet1.loc[mobile12][0]
            # # print(pavati)
            # Name=sheet1.loc[mobile12][1]
            # print(Name)
            # # date=sheet1.loc[mobile12][2]
            # # print(date)
            # unchi1=sheet1.loc[mobile12][3]=unchi11
            # sholder1=sheet1.loc[mobile12][4]
            # Astin1=sheet1.loc[mobile12][5]
            # kap1=sheet1.loc[mobile12][6]
            # gala1=sheet1.loc[mobile12][7]
            # chati1=sheet1.loc[mobile12][8]
            # pot1=sheet1.loc[mobile12][9]
            # sit1=sheet1.loc[mobile12][10]
            # front1=sheet1.loc[mobile12][11]
            # front2=sheet1.loc[mobile12][12]
            # front3=sheet1.loc[mobile12][13]
            # unchi2=sheet1.loc[mobile12][14]
            # kamar2=sheet1.loc[mobile12][15]
            # sit2=sheet1.loc[mobile12][16]
            # mandi2=sheet1.loc[mobile12][17]
            # chain2=sheet1.loc[mobile12][18]
            # gudaga2=sheet1.loc[mobile12][19]
            # botam2=sheet1.loc[mobile12][20]
            # shirt3=sheet1.loc[mobile12][21]
            # pant3=sheet1.loc[mobile12][22]
            # safari3=sheet1.loc[mobile12][23]
            # salavar3=sheet1.loc[mobile12][24]
            # shirtpis3=sheet1.loc[mobile12][25]
            # pantpis3=sheet1.loc[mobile12][26]
            # shirt33=sheet1.loc[mobile12][27]
            # pant33=sheet1.loc[mobile12][28]
            # safari33=sheet1.loc[mobile12][29]
            # salavar33=sheet1.loc[mobile12][30]
            # shirtpis33=sheet1.loc[mobile12][31]
            # pantpis33=sheet1.loc[mobile12][32]
            # discount33=sheet1.loc[mobile12][33]
            # total33=sheet1.loc[mobile12][34]
            # advance33=sheet1.loc[mobile12][35]
            # yene33=sheet1.loc[mobile12][36]

            # #_________________________________ 
            # pavati=sheet1.loc[mobile12][0]
            # print(pavati)
            sheet2.loc[mobile12,'Name']=shree11
            # date=sheet1.loc[mobile12][2]
            # print(date)
            sheet2.loc[mobile12,'unchi1']=unchi11
            sheet2.loc[mobile12,'sholder1']=sholder11
            sheet2.loc[mobile12,'Astin1']=astin11
            sheet2.loc[mobile12,'kap1']=kap11
            sheet2.loc[mobile12,'gala1']=gala11
            sheet2.loc[mobile12,'chati1']=chati11
            sheet2.loc[mobile12,'pot1']=pot11
            sheet2.loc[mobile12,'sit1']=sit11
            sheet2.loc[mobile12,'front1']=front11
            sheet2.loc[mobile12,'front2']=front12
            sheet2.loc[mobile12,'front3']=front13
            sheet2.loc[mobile12,'unchi2']=unchi22
            sheet2.loc[mobile12,'kamar2']=kamar22
            sheet2.loc[mobile12,'sit2']=sit22
            sheet2.loc[mobile12,'mandi2']=mandi22
            sheet2.loc[mobile12,'chain2']=chain22
            sheet2.loc[mobile12,'gudaga2']=gudgha22
            sheet2.loc[mobile12,'botam2']=bottom22
            #________________________________________
            
            # shirt3=sheet1.loc[mobile12][21]
            # pant3=sheet1.loc[mobile12][22]
            # safari3=sheet1.loc[mobile12][23]
            # salavar3=sheet1.loc[mobile12][24]
            # shirtpis3=sheet1.loc[mobile12][25]
            # pantpis3=sheet1.loc[mobile12][26]
            # shirt33=sheet1.loc[mobile12][27]
            # pant33=sheet1.loc[mobile12][28]
            # safari33=sheet1.loc[mobile12][29]
            # salavar33=sheet1.loc[mobile12][30]
            # shirtpis33=sheet1.loc[mobile12][31]
            # pantpis33=sheet1.loc[mobile12][32]
            # discount33=sheet1.loc[mobile12][33]
            # total33=sheet1.loc[mobile12][34]
            # advance33=sheet1.loc[mobile12][35]
            # yene33=sheet1.loc[mobile12][36]
            #_________________________________ 

            # #_________________________________ 
            # # pavati=sheet2.loc[mobile12][0]
            # # print(pavati)
            # sheet2.loc[mobile12][1]=Name
            # # date=sheet2.loc[mobile12][2]
            # # print(date)
            # sheet2.loc[mobile12,3]=unchi11
            # sheet2.loc[mobile12,4]=sholder11
            # sheet2.loc[mobile12,5]=astin11
            # sheet2.loc[mobile12,6]=kap11
            # sheet2.loc[mobile12,7]=gala11
            # sheet2.loc[mobile12,8]=chati11
            # sheet2.loc[mobile12,9]=pot11
            # sheet2.loc[mobile12,10]=sit11
            # sheet2.loc[mobile12,11]=front11
            # sheet2.loc[mobile12,12]=front12
            # sheet2.loc[mobile12,13]=front13
            # sheet2.loc[mobile12,14]=unchi22
            # sheet2.loc[mobile12,15]=kamar22
            # sheet2.loc[mobile12,16]=sit22
            # sheet2.loc[mobile12,17]=mandi22
            # sheet2.loc[mobile12,18]=chain22
            # sheet2.loc[mobile12,19]=gudgha22
            # sheet2.loc[mobile12,20]=bottom22

            sheet2.to_excel(path_measurements, sheet_name = "Sheet1") 
            print_bill()

        def canvas_3():
            
                    #_________main bil__________
            shirt55,pant55,safari55,salvar55,shirtpis55,pantpis55,shirt77,pant77,safari77,salvar77,shirtpis77,pantpis77,advance55,yene55,discount55,ekun33=total3()
            # advance55=int(advance33.get())
            # yene55=int(yene33.get())
            print(shirt55,pant55,safari55,salvar55,shirtpis55,pantpis55,discount55, ekun33,yene55,advance55)

            shirt5 = int(shirt3.get())
            pant5 = int(pant3.get())
            safari5 = int(safari3.get())
            salvar5 = int(salvar3.get())
            shirtpis5 = int(shirtpis3.get())
            pantpis5 = int(pantpis3.get())
            print(shirt5,pant5,safari5,salvar5,shirtpis5,pantpis5)

            shree11 = shree1.get()
            mobile11 = int(mobile1.get())
            print(shree11,mobile11)

            #_______________shirt________________
            unchi11= unchi4.get()
            sholder11= sholder4.get()
            astin11= astin4.get()
            kap11= kaP4.get()
            gala11= gala4.get()
            chati11= chati4.get()
            pot11= pot4.get()
            sit11= sit4.get()
            front11= front4.get()
            front12= front444.get()
            front13= front4444.get()
            print(unchi11,sholder11,astin11,kap11,gala11,chati11,pot11,sit11,front11,front111,front1111)

            #_______________pant_________________
            unchi22 = unchi5.get()
            kamar22 = kamar5.get()
            sit22 = sit5.get()
            mandi22 = mandi5.get()
            chain22 = chain5.get()
            gudgha22 = gudgha5.get()
            bottom22 = bottom5.get()
            print(unchi22,kamar22,sit22,mandi22,chain22,gudgha22,bottom22)


            #__________________canvas for values put in pdf_____________________________________
            canvas = cn("pdfFiles//print1.pdf", pagesize=LETTER)
            # Set font to Times New Roman with 12-point size
            canvas.setFont("Times-Roman", 10)

            #___________________counter____________________________________________________
            sheet1 = pds.read_excel(path_pavatinumber, sheet_name = "Sheet1") 
            sheet1.set_index('index', inplace = True)
            counter1=sheet1.loc[0][0]
            counter1+=1
            print(counter1) 
            sheet1.loc[0][0]= counter1
            sheet1.to_excel(path_pavatinumber, sheet_name = "Sheet1")
            pn1=counter1

            # pn3 = Label(text="##########",font=("calibre", font1, 'normal'),background=background1,foreground="white")
            # pn2 = Label(text=pn1,font=("calibre", font1, 'normal'),background=background1,foreground="black")
            # pn3.place(x=855 ,y=172)
            # pn2.place(x=855 ,y=172)
            # print(pn1)

        
            #___________________shirt__________________
            # Draw blue text one inch from the left and ten # inches from the bottom

            canvas.drawString(2 * cm, 25.4 * cm, str(pn1)) 
            canvas.drawString(2 * cm, 24.9 * cm, str(shree11)) 
            canvas.drawString(2 * cm, 24.3 * cm, str(mobile11)) 
            canvas.drawString(6.5 * cm, 24.3 * cm, str(date1)) 
            canvas.drawString(2.2 * cm, 23.1 * cm, str(unchi11)) 
            canvas.drawString(3.7 * cm, 23.1 * cm, str(sholder11)) 
            canvas.drawString(5.3 * cm, 23.1 * cm, str(astin11)) 
            canvas.drawString(6.9 * cm, 23.1 * cm, str(kap11)) 
            canvas.drawString(2.2 * cm, 21.9 * cm, str(gala11)) 
            canvas.drawString(3.7 * cm, 21.9 * cm, str(chati11)) 
            canvas.drawString(5.3 * cm, 21.9 * cm, str(pot11)) 
            canvas.drawString(6.9 * cm, 21.9 * cm, str(sit11)) 
            canvas.drawString(2.2 * cm, 20.7 * cm, str(front11)) 
            canvas.drawString(2.2 * cm, 20.2 * cm, str(front12)) 
            canvas.drawString(2.2 * cm, 19.6 * cm, str(front13))
            canvas.drawString(2.2 * cm, 19.1 * cm, str(shirtDiscription22.get()))
            #____________________pant______________________________

            canvas.drawString(2 * cm, 17.4 * cm, str(pn1)) 
            canvas.drawString(6.5 * cm, 17.4 * cm, str(date1))
            canvas.drawString(2.2 * cm, 16.2 * cm, str(unchi22)) 
            canvas.drawString(3.7 * cm, 16.2 * cm, str(kamar22)) 
            canvas.drawString(5.3 * cm, 16.2 * cm, str(sit22)) 
            canvas.drawString(6.9 * cm, 16.2 * cm, str(mandi22)) 
            canvas.drawString(2.2 * cm, 15 * cm, str(chain22)) 
            canvas.drawString(3.7 * cm, 15 * cm, str(gudgha22)) 
            canvas.drawString(5.3 * cm, 15 * cm, str(bottom22)) 
            canvas.drawString(2.2 * cm, 14.5 * cm, str(pantDiscription22.get()))

            #_______________main bill______________________________

            canvas.drawString(11.2 * cm, 24.3 * cm, str(pn1)) 
            canvas.drawString(11.2 * cm, 23.7 * cm, str(shree11)) 
            canvas.drawString(11.2* cm, 23.1 * cm, str(mobile11)) 
            canvas.drawString(16 * cm, 23.1 * cm, str(date1))
            
            canvas.drawString(16 * cm, 21.3 * cm, str(shirt5))
            canvas.drawString(16 * cm, 20.7 * cm, str(pant5))
            canvas.drawString(16 * cm, 20.1 * cm, str(safari5))
            canvas.drawString(16 * cm, 19.6 * cm, str(salvar5))
            canvas.drawString(16 * cm, 19 * cm, str(shirtpis5))
            canvas.drawString(16 * cm, 18.5 * cm, str(pantpis5))
        
            canvas.drawString(17 * cm, 21.3 * cm, str(shirt55))
            canvas.drawString(17 * cm, 20.7 * cm, str(pant55))
            canvas.drawString(17 * cm, 20.1 * cm, str(safari55))
            canvas.drawString(17 * cm, 19.6 * cm, str(salvar55))
            canvas.drawString(17 * cm, 19 * cm, str(shirtpis55))
            canvas.drawString(17 * cm, 18.5 * cm, str(pantpis55))

            canvas.drawString(18.3 * cm, 21.3 * cm, str(shirt77))
            canvas.drawString(18.3 * cm, 20.7 * cm, str(pant77))
            canvas.drawString(18.3 * cm, 20.1 * cm, str(safari77))
            canvas.drawString(18.3 * cm, 19.6 * cm, str(salvar77))
            canvas.drawString(18.3 * cm, 19 * cm, str(shirtpis77))
            canvas.drawString(18.3 * cm, 18.5 * cm, str(pantpis77))
        
            canvas.drawString(18.3 * cm, 17.9 * cm, str(discount55))
            canvas.drawString(18.3 * cm, 17.4 * cm, str(ekun33))
            canvas.drawString(18.3 * cm, 16.8 * cm, str(advance55))
            canvas.drawString(18.3 * cm, 16.2 * cm, str(yene55))
            # canvas.drawString(72, 72, "Hello, World")
            # Save the PDF file
            canvas.save()
            print("done")

            # print_bill()
            excel_3()
            #_____________________________________________________________________________________________________________
         
        # A = Canvas(root, bg ="white", height = 570, width = 585,relief=FLAT) 
        # A.place(x=158,y=162)
        # e = Canvas(root, bg =background2, height = 10, width = 585,relief=FLAT) 
        # e.place(x=158,y=430)

        print('search')
        sheet1 = pds.read_excel(path_measurements, sheet_name = "Sheet1") 
        sheet1.set_index('mobile ', inplace = True)
        # print(mobile1.get())

        mobile12=int(mobile1.get())
        print(mobile12)
        
        # pavati=sheet1.loc[mobile12][0]
        # print(pavati)
        Name=sheet1.loc[mobile12][1]
        print(Name)
        # date=sheet1.loc[mobile12][2]
        # print(date)
        unchi_1=sheet1.loc[mobile12][3]
        sholder_1=sheet1.loc[mobile12][4]
        Astin_1=sheet1.loc[mobile12][5]
        kap_1=sheet1.loc[mobile12][6]
        gala_1=sheet1.loc[mobile12][7]
        chati_1=sheet1.loc[mobile12][8]
        pot_1=sheet1.loc[mobile12][9]
        sit_1=sheet1.loc[mobile12][10]
        front_1=sheet1.loc[mobile12][11]
        front_2=sheet1.loc[mobile12][12]
        front_3=sheet1.loc[mobile12][13]
        unchi_2=sheet1.loc[mobile12][14]
        kamar_2=sheet1.loc[mobile12][15]
        sit_2=sheet1.loc[mobile12][16]
        mandi_2=sheet1.loc[mobile12][17]
        chain_2=sheet1.loc[mobile12][18]
        gudaga_2=sheet1.loc[mobile12][19]
        botam_2=sheet1.loc[mobile12][20]
        # shirt3=sheet1.loc[mobile12][21]
        # pant3=sheet1.loc[mobile12][22]
        # safari3=sheet1.loc[mobile12][23]
        # salavar3=sheet1.loc[mobile12][24]
        # shirtpis3=sheet1.loc[mobile12][25]
        # pantpis3=sheet1.loc[mobile12][26]
        # shirt33=sheet1.loc[mobile12][27]
        # pant33=sheet1.loc[mobile12][28]
        # safari33=sheet1.loc[mobile12][29]
        # salavar33=sheet1.loc[mobile12][30]
        # shirtpis33=sheet1.loc[mobile12][31]
        # pantpis33=sheet1.loc[mobile12][32]
        # discount33=sheet1.loc[mobile12][33]
        # total33=sheet1.loc[mobile12][34]
        # advance33=sheet1.loc[mobile12][35]
        # yene33=sheet1.loc[mobile12][36]

        unchi18=str(unchi_1)
        sholder18=str(sholder_1)
        Astin18=str(Astin_1)
        kap18=str(kap_1)
        gala18=str(gala_1)
        chati18=str(chati_1)
        pot18=str(pot_1)
        sit18=str(sit_1)
        front18=str(front_1)
        front28=str(front_2)
        front38=str(front_3)
        unchi28=str(unchi_2)
        kamar28=str(kamar_2)
        sit28=str(sit_2)
        mandi28=str(mandi_2)
        chain28=str(chain_2)
        gudaga28=str(gudaga_2)
        botam28=str(botam_2)
        # shirt38=str(shirt3)
        # pant38=str(pant3)
        # safari38=str(safari3)
        # salavar38=str(salavar3)
        # shirtpis38=str(shirtpis3)
        # shirtpis38=str(shirtpis3)
        # shirt338=str(shirt33)
        # pant338=str(pant33)
        # safari338=str(safari33)
        # salavar338=str(salavar33)
        # shirtpis338=str(shirtpis33)
        # pantpis338=str(pantpis33)
        # discount338=str(discount33)
        # total338=str(total33)
        # advance338=str(advance33)
        # yene338=str(yene33)
            
        #______________________shirt maesurement_____________________________________
        shirt11 = Label(text="x3R",font=("Marathi-Lekhani", 30, 'bold'),background=background1,foreground="black")
        unchi11 = Label(text="].cI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        sholder11 = Label(text="xoLDr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        astin11 = Label(text="AStIn",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        kaP11 = Label(text="kp",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        gala11 = Label(text="g;a",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        chati11 = Label(text="7atI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        pot11 = Label(text="po3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        sit11 = Label(text="sI3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        front11 = Label(text="f/N3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")

        shirt11.place(x=430 ,y=170)
        unchi11.place(x=208 ,y=220)
        sholder11.place(x=354 ,y=220)
        astin11.place(x=504 ,y=220)
        kaP11.place(x=662 ,y=220)
        gala11.place(x=210 ,y=290)
        chati11.place(x=355 ,y=290)
        pot11.place(x=510 ,y=290)
        sit11.place(x=660 ,y=290)
        front11.place(x=210 ,y=360)

        unchi4 = Entry(root, font=('calibre',font1,'normal'),width=6)
        unchi4.insert(0, unchi18)
        unchi4.pack()
        sholder4 = Entry(root,font=('calibre',font1,'normal'),width=6)
        sholder4.insert(0, sholder18)
        sholder4.pack()
        astin4= Entry(root,font=('calibre',font1,'normal'),width=6)
        astin4.insert(0, Astin18)
        astin4.pack()
        kaP4= Entry(root, font=('calibre',font1,'normal'),width=6)
        kaP4.insert(0, kap18)
        kaP4.pack()
        gala4= Entry(root, font=('calibre',font1,'normal'),width=6)
        gala4.insert(0, gala18)
        gala4.pack()
        chati4= Entry(root,font=('calibre',font1,'normal'),width=6)
        chati4.insert(0, chati18)
        chati4.pack()
        pot4= Entry(root, font=('calibre',font1,'normal'),width=6)
        pot4.insert(0, pot18)
        pot4.pack()
        sit4= Entry(root,font=('calibre',font1,'normal'),width=6)
        sit4.insert(0, sit18)
        sit4.pack()
        front4 = Entry(root, font=('calibre',font1,'normal'),width=6)
        front4.insert(0,front18)
        front4.pack()
        front444= Entry(root, font=('calibre',font1,'normal'),width=6)
        front444.insert(0, front28)
        front444.pack()
        front4444= Entry(root, font=('calibre',font1,'normal'),width=6)
        front4444.insert(0, front38)
        front4444.pack()

        unchi4.place(x=200 ,y=250)
        sholder4.place(x=350 ,y=250)
        astin4.place(x=500 ,y=250)
        kaP4.place(x=650 ,y=250)
        gala4.place(x=200 ,y=320)
        chati4.place(x=350 ,y=320)
        pot4.place(x=500 ,y=320)
        sit4.place(x=650 ,y=320)
        front4.place(x=200 ,y=390)
        front444.place(x=300 ,y=390)
        front4444.place(x=400 ,y=390)
        # front111.place(x=350 ,y=390)
        # front1111.place(x=500 ,y=390)

        shirtDiscription22= Entry(root, font=('calibre',font1,'normal'),width=23)
        shirtDiscription22.insert(0, "")
        shirtDiscription22.pack()
        shirtDiscription22.place(x=500 ,y=390)

        #__________pant___________________
        pant22 = Label(text="p>N3",font=("Marathi-Lekhani", 30, 'bold'),background=background1,foreground="black")
        unchi22 = Label(text="].cI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        kamar22 = Label(text="kmr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        sit22 = Label(text="sI3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        mandi22 = Label(text="ma.DI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        chain22 = Label(text="cEn",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        gudgha22 = Label(text="guDga",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        bottom22 = Label(text="ba>3m",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")

        pant22.place(x=430 ,y=450)
        unchi22.place(x=213 ,y=500)
        kamar22.place(x=361 ,y=500)
        sit22.place(x=513 ,y=500)
        mandi22.place(x=660 ,y=500)
        chain22.place(x=214 ,y=570)
        gudgha22.place(x=358 ,y=570)
        bottom22.place(x=509 ,y=570)

        unchi5 = Entry(root,font=('calibre',font1,'normal'),width=6)
        unchi5.insert(0, unchi28)
        unchi5.pack()
        kamar5 = Entry(root,font=('calibre',font1,'normal'),width=6)
        kamar5.insert(0, kamar28)
        kamar5.pack()
        sit5= Entry(root,font=('calibre',font1,'normal'),width=6)
        sit5.insert(0, sit28)
        sit5.pack()
        mandi5= Entry(root, font=('calibre',font1,'normal'),width=6)
        mandi5.insert(0, mandi28)
        mandi5.pack()
        chain5= Entry(root, font=('calibre',font1,'normal'),width=6)
        chain5.insert(0, chain28)
        chain5.pack()
        gudgha5= Entry(root,font=('calibre',font1,'normal'),width=6)
        gudgha5.insert(0, gudaga28)
        gudgha5.pack()
        bottom5= Entry(root,font=('calibre',font1,'normal'),width=6)
        bottom5.insert(0, botam28)
        bottom5.pack()

        unchi5.place(x=200 ,y=530)
        kamar5.place(x=350 ,y=530)
        sit5.place(x=500 ,y=530)
        mandi5.place(x=650 ,y=530)
        chain5.place(x=200 ,y=600)
        gudgha5.place(x=350 ,y=600)
        bottom5.place(x=500 ,y=600)

        pantDiscription22= Entry(root, font=('calibre',font1,'normal'),width=23)
        pantDiscription22.insert(0, "")
        pantDiscription22.pack()
        pantDiscription22.place(x=500 ,y=640)
        
        # #_______________main bill___________________________
        # pn11 = Label(text="Paa|n.|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        # shree11 = Label(text="&I|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        # mobile11 = Label(text="mo|n.| ",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        # date11 = Label(text="idna.k:",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        # pn11.place(x=800 ,y=170)
        # shree11.place(x=800 ,y=200)
        # mobile11.place(x=800 ,y=230)
        # date11.place(x=1100 ,y=230)

        # shree1_var =StringVar() 
        # mobile1_var =StringVar() 
        shree1 = Entry(root, font=('calibre',font1,'normal'),width=25)
        shree1.insert(0, Name)
        shree1.pack()
        # shree1 = Label(text=Name,font=('calibre',font1,'normal'),background=background1,foreground="black")
        date111 = Label(text=date1,font=("calibre", font1, 'normal'),background=background1,foreground="black")

        shree1.place(x=855 ,y=202)
        date111.place(x=1160 ,y=234)

        #||||||||||||||||
        m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
        m.place(x=800,y=270)
        m = Canvas(root, bg ="black", height = 215, width = 2,highlightthickness=0) 
        m.place(x=880,y=270)
        m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
        m.place(x=1104,y=270)
        m = Canvas(root, bg ="black", height = 215, width = 2,highlightthickness=0) 
        m.place(x=1166,y=270)
        m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
        m.place(x=1229,y=270)
        m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
        m.place(x=1292,y=270)

        # -------------------
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) #, bd=0, relief='ridge'
        m.place(x=800,y=270)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) #, bd=0, relief='ridge'
        m.place(x=800,y=305)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
        m.place(x=800,y=335)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
        m.place(x=800,y=365)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
        m.place(x=800,y=395)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
        m.place(x=800,y=425)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
        m.place(x=800,y=455)
        m = Canvas(root, bg ="black", height = 3, width = 494, highlightthickness=0) 
        m.place(x=800,y=485)
        m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
        m.place(x=1104,y=515)
        m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
        m.place(x=1104,y=545)
        m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
        m.place(x=1104,y=575)
        m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
        m.place(x=800,y=605)
        
        an1 = Label(text="A|n.|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        tapashil1 = Label(text="tpxIl",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        nag1 = Label(text="ng",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        dar1 = Label(text="dr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        rupaye1 = Label(text="+pye",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
        an1.place(x=819,y=272)
        tapashil1.place(x=960,y=272)
        nag1.place(x=1120,y=272)
        dar1.place(x=1184,y=272)
        rupaye1.place(x=1240,y=272)

        an11 = Label(text="1",font=("calibre", font1, 'bold'),background=background1,foreground="black")
        an11.place(x=830,y=308)
        an12 = Label(text="2",font=("calibre", font1, 'bold'),background=background1,foreground="black")
        an12.place(x=830,y=338)
        an13 = Label(text="3",font=("calibre", font1, 'bold'),background=background1,foreground="black")
        an13.place(x=830,y=368)
        an14 = Label(text="4",font=("calibre", font1, 'bold'),background=background1,foreground="black")
        an14.place(x=830,y=398)
        an15 = Label(text="5",font=("calibre", font1, 'bold'),background=background1,foreground="black")
        an15.place(x=830,y=428)
        an16 = Label(text="6",font=("calibre", font1, 'bold'),background=background1,foreground="black")
        an16.place(x=830,y=458)

        shirt4 = Label(text="x3R",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        pant4 = Label(text="p>3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        safari4= Label(text="sfarI",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        salvar4= Label(text="slvar",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        shirtpis4= Label(text="x3R pIs",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        pantpis4= Label(text="p>3 pIs",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        shirt4.place(x=900,y=308)
        pant4.place(x=900,y=338)
        safari4.place(x=900,y=368)
        salvar4.place(x=900,y=398)
        shirtpis4.place(x=900,y=428)
        pantpis4.place(x=900,y=458)

        discount4= Label(text="DISka].3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        ekun4= Label(text="0ku`",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        advance4= Label(text="ADVHaNs",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        yene4= Label(text="ye`e",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
        
        discount4.place(x=1120,y=488)
        ekun4.place(x=1130,y=518)
        advance4.place(x=1120,y=548)
        yene4.place(x=1135,y=578)
        
        #_______________nag , rupay entry____________________
    
        shirt3 = Entry(root,font=('calibre',14,'normal'),width=5)
        shirt3.insert(0, "0")
        shirt3.pack()
        shirt33 = Entry(root,font=('calibre',14,'normal'),width=5)
        shirt33.insert(0, "0")
        shirt33.pack()
        pant3 = Entry(root,font=('calibre',14,'normal'),width=5)
        pant3.insert(0, "0")
        pant3.pack()
        pant33 = Entry(root,font=('calibre',14,'normal'),width=5)
        pant33.insert(0, "0")
        pant33.pack()
        safari3 = Entry(root,font=('calibre',14,'normal'),width=5)
        safari3.insert(0, "0")
        safari3.pack()
        safari33 = Entry(root,font=('calibre',14,'normal'),width=5)
        safari33.insert(0, "0")
        safari33.pack()
        salvar3 = Entry(root,font=('calibre',14,'normal'),width=5)
        salvar3.insert(0, "0")
        salvar3.pack()
        salvar33 = Entry(root, font=('calibre',14,'normal'),width=5)
        salvar33.insert(0, "0")
        salvar33.pack()
        shirtpis3 = Entry(root, font=('calibre',14,'normal'),width=5)
        shirtpis3.insert(0, "0")
        shirtpis3.pack()
        shirtpis33 = Entry(root, font=('calibre',14,'normal'),width=5)
        shirtpis33.insert(0, "0")
        shirtpis33.pack()
        pantpis3 = Entry(root,font=('calibre',14,'normal'),width=5)
        pantpis3.insert(0, "0")
        pantpis3.pack()
        pantpis33 = Entry(root, font=('calibre',14,'normal'),width=5)
        pantpis33.insert(0, "0")
        pantpis33.pack()
        discount33 = Entry(root, font=('calibre',14,'normal'),width=5)
        discount33.insert(0, "0")
        discount33.pack()
        advance33 = Entry(root, font=('calibre',14,'normal'),width=5)
        advance33.insert(0, "0")
        advance33.pack()
        # yene33 = Entry(root,font=('calibre',14,'normal'),width=5)
        # yene33.insert(0, "0")
        # yene33.pack()

        shirt3.place(x=1104.5,y=307)
        shirt33.place(x=1168,y=307)
        pant3.place(x=1104.5,y=337)
        pant33.place(x=1168,y=337)
        safari3.place(x=1104.5,y=367)
        safari33.place(x=1168,y=367)
        salvar3.place(x=1104.5,y=397)
        salvar33.place(x=1168,y=397)
        shirtpis3.place(x=1104.5,y=427)
        shirtpis33.place(x=1168,y=427)
        pantpis3.place(x=1104.5,y=457)
        pantpis33.place(x=1168,y=457)
        discount33.place(x=1230.5,y=487)
        advance33.place(x=1230.5,y=547)
        # yene33.place(x=1230.5,y=577)

        button3 = Button(root, text = "Save",style = 'W.TButton',command = total3)
        button3.place(x=1180,y=635)

        button5 = Button(root, text = "Search",style = 'E.TButton',command = search1)
        button5.place(x=988,y=229)
#___________________________________________________________________________________________________________-
    A = Canvas(root, bg ="white", height = 570, width = 1216,relief=FLAT) 
    A.place(x=158,y=160)
    d = Canvas(root, bg =background2, height = 570, width = 10,relief=FLAT) 
    d.place(x=745,y=160)
    c = Canvas(root, bg =background2, height = 10, width = 1216,relief=FLAT) 
    c.place(x=158,y=150)
    e = Canvas(root, bg =background2, height = 10, width = 585,relief=FLAT) 
    e.place(x=158,y=430)
    
    #________________couter______________________________________________________
    # sheet1 = pds.read_excel('ExcelFiles//pavatinumber.xlsx', sheet_name = "Sheet1") 
    # sheet1.set_index('index', inplace = True)
    # counter1=sheet1.loc[0][0]
    # counter1+=1
    # print(counter1) 
    # sheet1.loc[0][0]=counter1
    # sheet1.to_excel('ExcelFiles//pavatinumber.xlsx', sheet_name = "Sheet1") 


    #______________________shirt maesurement_____________________________________
    shirt11 = Label(text="x3R",font=("Marathi-Lekhani", 30, 'bold'),background=background1,foreground="black")
    unchi11 = Label(text="].cI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    sholder11 = Label(text="xoLDr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    astin11 = Label(text="AStIn",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    kaP11 = Label(text="kp",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    gala11 = Label(text="g;a",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    chati11 = Label(text="7atI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    pot11 = Label(text="po3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    sit11 = Label(text="sI3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    front11 = Label(text="f/N3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")

    shirt11.place(x=430 ,y=170)
    unchi11.place(x=208 ,y=220)
    sholder11.place(x=354 ,y=220)
    astin11.place(x=504 ,y=220)
    kaP11.place(x=662 ,y=220)
    gala11.place(x=210 ,y=290)
    chati11.place(x=355 ,y=290)
    pot11.place(x=510 ,y=290)
    sit11.place(x=660 ,y=290)
    front11.place(x=210 ,y=360)
    

    unchi1 = Entry(root, font=('calibre',font1,'normal'),width=6)
    unchi1.insert(0, "0")
    unchi1.pack()
    sholder1 = Entry(root,font=('calibre',font1,'normal'),width=6)
    sholder1.insert(0, "0")
    sholder1.pack()
    astin1= Entry(root,font=('calibre',font1,'normal'),width=6)
    astin1.insert(0, "0")
    astin1.pack()
    kaP1= Entry(root, font=('calibre',font1,'normal'),width=6)
    kaP1.insert(0, "0")
    kaP1.pack()
    gala1= Entry(root, font=('calibre',font1,'normal'),width=6)
    gala1.insert(0, "0")
    gala1.pack()
    chati1= Entry(root,font=('calibre',font1,'normal'),width=6)
    chati1.insert(0, "0")
    chati1.pack()
    pot1= Entry(root, font=('calibre',font1,'normal'),width=6)
    pot1.insert(0, "0")
    pot1.pack()
    sit1= Entry(root,font=('calibre',font1,'normal'),width=6)
    sit1.insert(0, "0")
    sit1.pack()
    front1= Entry(root, font=('calibre',font1,'normal'),width=6)
    front1.insert(0, "0")
    front1.pack()
    front111= Entry(root, font=('calibre',font1,'normal'),width=6)
    front111.insert(0, "0")
    front111.pack()
    front1111= Entry(root, font=('calibre',font1,'normal'),width=6)
    front1111.insert(0, "0")
    front1111.pack()
    
    shirtDiscription1111= Entry(root, font=('calibre',font1,'normal'),width=23)
    shirtDiscription1111.insert(0, "")
    shirtDiscription1111.pack()
    shirtDiscription1111.place(x=500 ,y=390)

    unchi1.place(x=200 ,y=250)
    sholder1.place(x=350 ,y=250)
    astin1.place(x=500 ,y=250)
    kaP1.place(x=650 ,y=250)
    gala1.place(x=200 ,y=320)
    chati1.place(x=350 ,y=320)
    pot1.place(x=500 ,y=320)
    sit1.place(x=650 ,y=320)
    front1.place(x=200 ,y=390)
    front111.place(x=300 ,y=390)
    front1111.place(x=400 ,y=390)
    # front111.place(x=350 ,y=390)
    # front1111.place(x=500 ,y=390)



    #__________pant___________________
    pant22 = Label(text="p>N3",font=("Marathi-Lekhani", 30, 'bold'),background=background1,foreground="black")
    unchi22 = Label(text="].cI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    kamar22 = Label(text="kmr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    sit22 = Label(text="sI3",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    mandi22 = Label(text="ma.DI",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    chain22 = Label(text="cEn",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    gudgha22 = Label(text="guDga",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    bottom22 = Label(text="ba>3m",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")

    pant22.place(x=430 ,y=450)
    unchi22.place(x=213 ,y=500)
    kamar22.place(x=361 ,y=500)
    sit22.place(x=513 ,y=500)
    mandi22.place(x=660 ,y=500)
    chain22.place(x=214 ,y=570)
    gudgha22.place(x=358 ,y=570)
    bottom22.place(x=509 ,y=570)

    unchi2 = Entry(root,font=('calibre',font1,'normal'),width=6)
    unchi2.insert(0, "0")
    unchi2.pack()
    kamar2 = Entry(root,font=('calibre',font1,'normal'),width=6)
    kamar2.insert(0, "0")
    kamar2.pack()
    sit2= Entry(root,font=('calibre',font1,'normal'),width=6)
    sit2.insert(0, "0")
    sit2.pack()
    mandi2= Entry(root, font=('calibre',font1,'normal'),width=6)
    mandi2.insert(0, "0")
    mandi2.pack()
    chain2= Entry(root, font=('calibre',font1,'normal'),width=6)
    chain2.insert(0, "0")
    chain2.pack()
    gudgha2= Entry(root,font=('calibre',font1,'normal'),width=6)
    gudgha2.insert(0, "0")
    gudgha2.pack()
    bottom2= Entry(root,font=('calibre',font1,'normal'),width=6)
    bottom2.insert(9, "0")
    bottom2.pack()

    pantDiscription1111= Entry(root, font=('calibre',font1,'normal'),width=23)
    pantDiscription1111.insert(0, "")
    pantDiscription1111.pack()
    pantDiscription1111.place(x=500 ,y=640)

    unchi2.place(x=200 ,y=530)
    kamar2.place(x=350 ,y=530)
    sit2.place(x=500 ,y=530)
    mandi2.place(x=650 ,y=530)
    chain2.place(x=200 ,y=600)
    gudgha2.place(x=350 ,y=600)
    bottom2.place(x=500 ,y=600)

    
    #_______________main bill___________________________
    pn11 = Label(text="Paa|n.|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    shree11 = Label(text="&I|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    mobile11 = Label(text="mo|n.| ",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    date11 = Label(text="idna.k:",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    pn11.place(x=800 ,y=170)
    shree11.place(x=800 ,y=200)
    mobile11.place(x=800 ,y=230)
    date11.place(x=1100 ,y=230)

    # shree1_var =StringVar() 
    # mobile1_var =StringVar() 

    shree1 = Entry(root,font=('calibre',font1,'normal'),width=25)
    shree1.insert(0, "")
    shree1.pack()
    mobile1 = Entry(root, font=('calibre',font1,'normal'),width=13) #textvariable = mobile1_var,
    mobile1.insert(0, "0")
    mobile1.pack()
    date111 = Label(text=date1,font=("calibre", font1, 'normal'),background=background1,foreground="black")

    shree1.place(x=855 ,y=202)
    mobile1.place(x=855 ,y=232)
    date111.place(x=1160 ,y=234)

    #||||||||||||||||
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=800,y=270)
    m = Canvas(root, bg ="black", height = 215, width = 2,highlightthickness=0) 
    m.place(x=880,y=270)
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=1104,y=270)
    m = Canvas(root, bg ="black", height = 215, width = 2,highlightthickness=0) 
    m.place(x=1166,y=270)
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=1229,y=270)
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=1292,y=270)

    # -------------------
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) #, bd=0, relief='ridge'
    m.place(x=800,y=270)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) #, bd=0, relief='ridge'
    m.place(x=800,y=305)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=335)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=365)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=395)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=425)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=455)
    m = Canvas(root, bg ="black", height = 3, width = 494, highlightthickness=0) 
    m.place(x=800,y=485)
    m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
    m.place(x=1104,y=515)
    m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
    m.place(x=1104,y=545)
    m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
    m.place(x=1104,y=575)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=605)
    
    an1 = Label(text="A|n.|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    tapashil1 = Label(text="tpxIl",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    nag1 = Label(text="ng",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    dar1 = Label(text="dr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    rupaye1 = Label(text="+pye",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    an1.place(x=819,y=272)
    tapashil1.place(x=960,y=272)
    nag1.place(x=1120,y=272)
    dar1.place(x=1184,y=272)
    rupaye1.place(x=1240,y=272)

    an11 = Label(text="1",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an11.place(x=830,y=308)
    an12 = Label(text="2",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an12.place(x=830,y=338)
    an13 = Label(text="3",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an13.place(x=830,y=368)
    an14 = Label(text="4",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an14.place(x=830,y=398)
    an15 = Label(text="5",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an15.place(x=830,y=428)
    an16 = Label(text="6",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an16.place(x=830,y=458)

    shirt4 = Label(text="x3R",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    pant4 = Label(text="p>3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    safari4= Label(text="sfarI",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    salvar4= Label(text="slvar",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    shirtpis4= Label(text="x3R pIs",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    pantpis4= Label(text="p>3 pIs",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    shirt4.place(x=900,y=308)
    pant4.place(x=900,y=338)
    safari4.place(x=900,y=368)
    salvar4.place(x=900,y=398)
    shirtpis4.place(x=900,y=428)
    pantpis4.place(x=900,y=458)

    discount4= Label(text="DISka].3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    ekun4= Label(text="0ku`",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    advance4= Label(text="ADVHaNs",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    yene4= Label(text="ye`e",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    
    discount4.place(x=1120,y=488)
    ekun4.place(x=1130,y=518)
    advance4.place(x=1120,y=548)
    yene4.place(x=1135,y=578)
    
    #_______________nag , rupay entry____________________
 
    def callback(sv1,sv):
        prod=int(sv1.get())*int(sv.get())
        prod1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        prod1.place(x=1230.5,y=307)
        prod1= Label(text=prod,font=("calibre", font, 'bold'),background=background1,foreground="black")
        prod1.place(x=1230.5,y=307)
        return prod
    shirt3_var=StringVar()
    shirt3 = Entry(root,textvariable=shirt3_var,font=('calibre',14,'normal'),width=5)
    shirt3.insert(0, "0")
    shirt3.pack()
    shirt33_var=StringVar()
    shirt33_var.trace("w", lambda name, index, mode, shirt33_var=shirt33_var: callback(shirt33_var,shirt3_var))
    shirt33 = Entry(root,textvariable=shirt33_var,font=('calibre',14,'normal'),width=5)
    shirt33.insert(0, "0")
    shirt33.pack()


    def callback1(sv1,sv):
        prod=int(sv1.get())*int(sv.get())
        prod1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        prod1.place(x=1230.5,y=337)
        prod1= Label(text=prod,font=("calibre", font, 'bold'),background=background1,foreground="black")
        prod1.place(x=1230.5,y=337)
        return prod
    pant3_var=StringVar()
    pant3 = Entry(root,textvariable=pant3_var,font=('calibre',14,'normal'),width=5)
    pant3.insert(0, "0")
    pant3.pack()
    pant33_var=StringVar()
    pant33_var.trace("w", lambda name, index, mode, pant33_var=pant33_var: callback1(pant33_var,pant3_var))
    pant33 = Entry(root,textvariable=pant33_var,font=('calibre',14,'normal'),width=5)
    pant33.insert(0, "0")
    pant33.pack()

    def callback2(sv1,sv):
        prod=int(sv1.get())*int(sv.get())
        prod1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        prod1.place(x=1230.5,y=367)
        prod1= Label(text=prod,font=("calibre", font, 'bold'),background=background1,foreground="black")
        prod1.place(x=1230.5,y=367)
        return prod
    safari3_var=StringVar()
    safari3 = Entry(root,textvariable=safari3_var,font=('calibre',14,'normal'),width=5)
    safari3.insert(0, "0")
    safari3.pack()
    safari33_var=StringVar()
    safari33_var.trace("w", lambda name, index, mode, safari33_var=safari33_var: callback2(safari33_var,safari3_var))
    safari33 = Entry(root,textvariable=safari33_var,font=('calibre',14,'normal'),width=5)
    safari33.insert(0, "0")
    safari33.pack()

    def callback3(sv1,sv):
        prod=int(sv1.get())*int(sv.get())
        prod1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        prod1.place(x=1230.5,y=397)
        prod1= Label(text=prod,font=("calibre", font, 'bold'),background=background1,foreground="black")
        prod1.place(x=1230.5,y=397)
        return prod
    salvar3_var=StringVar()
    salvar3 = Entry(root,textvariable=salvar3_var,font=('calibre',14,'normal'),width=5)
    salvar3.insert(0, "0")
    salvar3.pack()
    salvar33_var=StringVar()
    salvar33_var.trace("w", lambda name, index, mode, salvar33_var=salvar33_var: callback3(salvar33_var,salvar3_var))
    salvar33 = Entry(root, textvariable=salvar33_var,font=('calibre',14,'normal'),width=5)
    salvar33.insert(0, "0")
    salvar33.pack()

    def callback4(sv1,sv):
        prod=int(sv1.get())*int(sv.get())
        prod1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        prod1.place(x=1230.5,y=427)
        prod1= Label(text=prod,font=("calibre", font, 'bold'),background=background1,foreground="black")
        prod1.place(x=1230.5,y=427)
        return prod
    shirtpis3_var=StringVar()
    shirtpis3 = Entry(root, textvariable=shirtpis3_var, font=('calibre',14,'normal'),width=5)
    shirtpis3.insert(0, "0")
    shirtpis3.pack()
    shirtpis33_var=StringVar()
    shirtpis33_var.trace("w", lambda name, index, mode, shirtpis33_var=shirtpis33_var: callback4(shirtpis33_var,shirtpis3_var))
    shirtpis33 = Entry(root, textvariable=shirtpis33_var, font=('calibre',14,'normal'),width=5)
    shirtpis33.insert(0, "0")
    shirtpis33.pack()

    def callback5(sv1,sv):
        prod5=int(sv1.get())*int(sv.get())
        prod11= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        prod11.place(x=1230.5,y=457)
        prod11= Label(text=prod5,font=("calibre", font, 'bold'),background=background1,foreground="black")
        prod11.place(x=1230.5,y=457)

        prod0=callback()
        prod1=callback1()
        prod2=callback2()
        prod3=callback3()
        prod4=callback4()

        sum=prod0+prod1+prod2+prod3+prod4+prod5
        sum1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
        sum1.place(x=1232,y=517)
        sum1= Label(text=sum,font=("calibre", font, 'bold'),background=background1,foreground="black")
        sum1.place(x=1232,y=517)

    pantpis3_var=StringVar()
    pantpis3 = Entry(root, textvariable=pantpis3_var,font=('calibre',14,'normal'),width=5)
    pantpis3.insert(0, "0")
    pantpis3.pack()
    pantpis33_var=StringVar()
    pantpis33_var.trace("w", lambda name, index, mode, pantpis33_var=pantpis33_var: callback5(pantpis33_var,pantpis3_var))
    pantpis33 = Entry(root, textvariable=pantpis33_var, font=('calibre',14,'normal'),width=5)
    pantpis33.insert(0, "0")
    pantpis33.pack()

    # def callback5(sv1,sv):
    #     prod=int(sv1.get())*int(sv.get())
    #     prod1= Label(text="#####",font=("calibre", font, 'bold'),background=background1,foreground="white")
    #     prod1.place(x=1230.5,y=307)
    #     prod1= Label(text=prod,font=("calibre", font, 'bold'),background=background1,foreground="black")
    #     prod1.place(x=1230.5,y=307)
    # pantpis3_var=StringVar()
    discount33 = Entry(root, font=('calibre',14,'normal'),width=5)
    discount33.insert(0, "0")
    discount33.pack()
    advance33 = Entry(root, font=('calibre',14,'normal'),width=5)
    advance33.insert(0, "0")
    advance33.pack()

    # yene33 = Entry(root,font=('calibre',14,'normal'),width=5)
    # yene33.insert(0, "0")
    # yene33.pack()

    shirt3.place(x=1104.5,y=307)
    shirt33.place(x=1168,y=307)
    pant3.place(x=1104.5,y=337)
    pant33.place(x=1168,y=337)
    safari3.place(x=1104.5,y=367)
    safari33.place(x=1168,y=367)
    salvar3.place(x=1104.5,y=397)
    salvar33.place(x=1168,y=397)
    shirtpis3.place(x=1104.5,y=427)
    shirtpis33.place(x=1168,y=427)
    pantpis3.place(x=1104.5,y=457)
    pantpis33.place(x=1168,y=457)
    discount33.place(x=1230.5,y=487)
    advance33.place(x=1230.5,y=547)
    # yene33.place(x=1230.5,y=577)

    button5 = Button(root, text = "Search",style = 'E.TButton',command = search1)
    button5.place(x=988,y=229)
    # button3 = Button(root, text = "Save",style = 'W.TButton',command = total1)
    button3 = Button(root, text = "Save",style = 'W.TButton',command = canvas_1)
    button3.place(x=1180,y=635)

def canvas_excel_2():
    def total1():
        shirt6=int(shirt3.get())
        pant6=int(pant3.get())
        Tshirt6=int(Tshirt3.get())
        nightpant6=int(nightpant3.get())
        bermuda6=int(bermuda3.get())
        underwear6=int(underwear3.get())
        baniyan6=int(baniyan3.get())
        salvar6=int(salvar3.get())

        shirt5=int(shirt33.get())
        pant5=int(pant33.get())
        Tshirt5=int(Tshirt33.get())
        nightpant5=int(nightpant33.get())
        bermuda5=int(bermuda33.get())
        underwear5=int(underwear33.get())
        baniyan5=int(baniyan33.get())
        salvar5=int(salvar33.get())
        discount5=int(discount33.get())

        shirt7 = shirt5*shirt6
        pant7 = pant5*pant6 
        Tshirt7 = Tshirt5*Tshirt6 
        nightpant7 =  nightpant5*nightpant6
        bermuda7 =  bermuda5*bermuda6
        underwear7 = underwear5*underwear6
        baniyan7 =  baniyan5*baniyan6
        salvar7 =  salvar5*salvar6      

        shirt333=Label(text=shirt7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        pant333=Label(text=pant7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        Tshirt333=Label(text=Tshirt7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        nightpant333=Label(text=nightpant7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        bermuda333=Label(text=bermuda7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        underwear333=Label(text=underwear7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        baniyan333=Label(text=baniyan7,font=("calibre", font, 'bold'),background=background1,foreground="black")
        salvar333=Label(text=salvar7,font=("calibre", font, 'bold'),background=background1,foreground="black")

        shirt333.place(x=1230.5,y=307)
        pant333.place(x=1230.5,y=337)
        Tshirt333.place(x=1230.5,y=367)
        nightpant333.place(x=1230.5,y=397)
        bermuda333.place(x=1230.5,y=427)
        underwear333.place(x=1230.5,y=457)
        baniyan333.place(x=1230.5,y=487)
        salvar333.place(x=1230.5,y=517)

        ekun33_var=shirt7 + pant7 + Tshirt7 + nightpant7 + bermuda7 + underwear7 + baniyan7 + salvar7
        print(ekun33_var)
        print(discount5)

        total = ekun33_var - (discount5 * ekun33_var)/100
        print(total)
        ekun333= Label(text=total,font=("calibre", font, 'bold'),background=background1,foreground="black")
        ekun333.place(x=1232,y=577)

        button4 = Button(root, text = "Print",style = 'W.TButton',command = canvas_2)
        button4.place(x=1000,y=635)

        return shirt5,pant5,Tshirt5,nightpant5,bermuda5,underwear5,baniyan5,salvar5,shirt7,pant7,Tshirt7,nightpant7,bermuda7,underwear7,baniyan7,salvar7,discount5,total

    '''
    def excel_2():
               #_________main bil__________
        shirt55,pant55,Tshirt55,nightpant55,bermuda55,underwear55,baniyan55,salvar55,shirt77,pant77,Tshirt77,nightpant77,bermuda77,underwear77,baniyan77,salvar77,discount55,ekun33=total1()

        shirt5 = int(shirt3.get())
        pant5 = int(pant3.get())
        Tshirt5 = int(Tshirt3.get())
        nightpant5 = int(nightpant3.get())
        bermuda5 = int(bermuda3.get())
        underwear5 = int(underwear3.get())
        baniyan5 = int(baniyan3.get())
        salvar5 = int(salvar3.get())

        shree11 = shree1.get()
        mobile11 = int(mobile1.get())





        print("excel")
        
        #________________counter_________________
        sheet1 = pds.read_excel('ExcelFiles//pavatinumber.xlsx', sheet_name = "Sheet1") 
        sheet1.set_index('index', inplace = True)
        counter1=sheet1.loc[0][0]

        pn1=counter1

        print("excel")
        sheet3 = pds.read_excel('ExcelFiles//shop_sales.xlsx', sheet_name = "Sheet1") 
        my_list2 = sheet3.columns.values.tolist()
        print(my_list2)

        print(shirt55,pant55,Tshirt55,nightpant55,bermuda55,underwear55,baniyan55,salvar55,discount55,ekun33)
        print(shirt5,pant5,Tshirt5,nightpant5,bermuda5,underwear5,baniyan5,salvar5)
        print(shree11,mobile11)
        df2=pds.DataFrame({'mobile':[mobile11],'date':[date1],'name':[shree11]
                        ,'shirt1':[shirt5],'pant1':[pant5],'Tshirt1':[Tshirt5]
                        ,'nightpant1':[nightpant5],'bermuda1':[bermuda5],'underwaer1':[underwear5]
                        ,'baniyan1':[baniyan5],'salvar1':[salvar5]
                        ,'shirt2':[shirt55],'pant2':[pant55],'Tshirt2':[Tshirt55]
                        ,'nightpant2':[nightpant55],'bermuda2':[bermuda55],'underwaer2':[underwear55]
                        ,'baniyan2':[baniyan55],'salvar2':[salvar55]
                        ,'shirt3':[shirt77],'pant3':[pant77],'Tshirt3':[Tshirt77]
                        ,'nightpant3':[nightpant77],'bermuda3':[bermuda77],'underwaer3':[underwear77]
                        ,'baniyan3':[baniyan77],'salvar3':[salvar77],'discaount2':[discount55],'total2':[ekun33]})
        print(df2)

        df3=sheet3.append(df2) 
        print(df3)

        df3.to_excel('ExcelFiles//shop_sales.xlsx', sheet_name = "Sheet1",index = False) 
        print_bill1()
    '''


    def canvas_2():
        
                #_________main bil__________
        shirt55,pant55,Tshirt55,nightpant55,bermuda55,underwear55,baniyan55,salvar55,shirt77,pant77,Tshirt77,nightpant77,bermuda77,underwear77,baniyan77,salvar77,discount55,ekun33=total1()
        print(shirt55,pant55,Tshirt55,nightpant55,bermuda55,underwear55,baniyan55,salvar55,shirt77,pant77,Tshirt77,nightpant77,bermuda77,underwear77,baniyan77,salvar77,discount55,ekun33)

        shirt5 = int(shirt3.get())
        pant5 = int(pant3.get())
        Tshirt5 = int(Tshirt3.get())
        nightpant5 = int(nightpant3.get())
        bermuda5 = int(bermuda3.get())
        underwear5 = int(underwear3.get())
        baniyan5 = int(baniyan3.get())
        salvar5 = int(salvar3.get())
        print(shirt5,pant5,Tshirt5,nightpant5,bermuda5,underwear5,baniyan5,salvar5)

        shree11 = shree1.get()
        mobile11 = int(mobile1.get())
        print(shree11,mobile11)


        #__________________canvas for values put in pdf_____________________________________
        canvas = cn("pdfFiles//print.pdf", pagesize=LETTER)
        # Set font to Times New Roman with 12-point size
        canvas.setFont("Times-Roman", 10)

        #_______________main bill______________________________

        canvas.drawString(2.5 * cm, 23.8 * cm, str(shree11)) 
        canvas.drawString(2.5 * cm, 23.2 * cm, str(mobile11)) 
        canvas.drawString(6.7 * cm, 23.2 * cm, str(date1))

        canvas.drawString(3 * cm, 21.6 * cm, str(an111.get()))
        canvas.drawString(3 * cm, 21.1 * cm, str(an112.get()))
        canvas.drawString(3 * cm, 20.5 * cm, str(an113.get()))
        canvas.drawString(3 * cm, 19.98 * cm, str(an114.get()))
        canvas.drawString(3 * cm, 19.43 * cm, str(an115.get()))
        canvas.drawString(3 * cm, 18.9 * cm, str(an116.get()))
        canvas.drawString(3 * cm, 18.3 * cm, str(an117.get()))
        canvas.drawString(3 * cm, 17.8 * cm, str(an118.get()))

        canvas.drawString(6.8 * cm, 21.6 * cm, str(shirt5))
        canvas.drawString(6.8 * cm, 21.1 * cm, str(pant5))
        canvas.drawString(6.8 * cm, 20.5 * cm, str(Tshirt5))
        canvas.drawString(6.8 * cm, 19.98 * cm, str(nightpant5))
        canvas.drawString(6.8 * cm, 19.43 * cm, str(bermuda5))
        canvas.drawString(6.8 * cm, 18.9 * cm, str(underwear5))
        canvas.drawString(6.8 * cm, 18.3 * cm, str(baniyan5))
        canvas.drawString(6.8* cm, 17.8 * cm, str(salvar5))

        canvas.drawString(7.7 * cm, 21.6 * cm, str(shirt55))
        canvas.drawString(7.7 * cm, 21.1 * cm, str(pant55))
        canvas.drawString(7.7 * cm, 20.5 * cm, str(Tshirt55))
        canvas.drawString(7.7 * cm, 19.98 * cm, str(nightpant55))
        canvas.drawString(7.7 * cm, 19.43 * cm, str(bermuda55))
        canvas.drawString(7.7 * cm, 18.9 * cm, str(underwear55))
        canvas.drawString(7.7 * cm, 18.3 * cm, str(baniyan55))
        canvas.drawString(7.7 * cm, 17.8 * cm, str(salvar55))

        canvas.drawString(8.9 * cm, 21.6 * cm, str(shirt77))
        canvas.drawString(8.9 * cm, 21.1 * cm, str(pant77))
        canvas.drawString(8.9 * cm, 20.5 * cm, str(Tshirt77))
        canvas.drawString(8.9 * cm, 19.98 * cm, str(nightpant77))
        canvas.drawString(8.9 * cm, 19.43 * cm, str(bermuda77))
        canvas.drawString(8.9 * cm, 18.9 * cm, str(underwear77))
        canvas.drawString(8.9 * cm, 18.3 * cm, str(baniyan77))
        canvas.drawString(8.9 * cm, 17.8 * cm, str(salvar77))
        canvas.drawString(8.9 * cm, 17.25 * cm, str(discount55))
        canvas.drawString(8.9 * cm, 16.7 * cm, str(ekun33))

        canvas.save()
        print("done")

        #excel_2()
        print_bill1()
        #_____________________________________________________________________________________________________________
#______________________________________________________________________________________________________________
    E = Canvas(root, bg ="white", height = 570, width = 1216,relief=FLAT) 
    E.place(x=158,y=160)

    #_______________main bill___________________________
    shree11 = Label(text="&I|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    mobile11 = Label(text="mo|n.| ",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    date11 = Label(text="idna.k:",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    shree11.place(x=800 ,y=200)
    mobile11.place(x=800 ,y=230)
    date11.place(x=1100 ,y=230)

    # shree1_var =StringVar() 
    # mobile1_var =StringVar() 

    shree1 = Entry(root,font=('calibre',font1,'normal'),width=25)
    shree1.insert(0, "")
    shree1.pack()
    mobile1 = Entry(root, font=('calibre',font1,'normal'),width=13) #textvariable = mobile1_var,
    mobile1.insert(0, "0")
    mobile1.pack()
    date111 = Label(text=date1,font=("calibre", font1, 'normal'),background=background1,foreground="black")
    shree1.place(x=855 ,y=202)
    mobile1.place(x=855 ,y=232)
    date111.place(x=1160 ,y=234)

    #||||||||||||||||
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=800,y=270)
    m = Canvas(root, bg ="black", height = 275, width = 2,highlightthickness=0) 
    m.place(x=880,y=270)
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=1103,y=270)
    m = Canvas(root, bg ="black", height = 275, width = 2,highlightthickness=0) 
    m.place(x=1166,y=270)
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=1229,y=270)
    m = Canvas(root, bg ="black", height = 335, width = 2,highlightthickness=0) 
    m.place(x=1292,y=270)

    # -------------------
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) #, bd=0, relief='ridge'
    m.place(x=800,y=270)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) #, bd=0, relief='ridge'
    m.place(x=800,y=305)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=335)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=365)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=395)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=425)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=455)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=485)
    m = Canvas(root, bg ="black", height = 2, width = 494, highlightthickness=0) 
    m.place(x=800,y=515)
    m = Canvas(root, bg ="black", height = 3, width = 494, highlightthickness=0) 
    m.place(x=800,y=545)
    m = Canvas(root, bg ="black", height = 2, width = 190, highlightthickness=0) 
    m.place(x=1104,y=575)
    m = Canvas(root, bg ="black", height = 3, width = 494, highlightthickness=0) 
    m.place(x=800,y=605)
    
    an1 = Label(text="A|n.|",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    tapashil1 = Label(text="tpxIl",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    nag1 = Label(text="ng",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    dar1 = Label(text="dr",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    rupaye1 = Label(text="+pye",font=("Marathi-Lekhani", font, 'bold'),background=background1,foreground="black")
    an1.place(x=819,y=272)
    tapashil1.place(x=960,y=272)
    nag1.place(x=1120,y=272)
    dar1.place(x=1185,y=272)
    rupaye1.place(x=1240,y=272)

    an11 = Label(text="1",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an11.place(x=830,y=308)
    an12 = Label(text="2",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an12.place(x=830,y=338)
    an13 = Label(text="3",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an13.place(x=830,y=368)
    an14 = Label(text="4",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an14.place(x=830,y=398)
    an15 = Label(text="5",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an15.place(x=830,y=428)
    an16 = Label(text="6",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an16.place(x=830,y=458)
    an17 = Label(text="7",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an17.place(x=830,y=488)
    an18 = Label(text="8",font=("calibre", font1, 'bold'),background=background1,foreground="black")
    an18.place(x=830,y=518)

    an111 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an111.insert(0, "")
    an111.pack()
    an112 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an112.insert(0, "")
    an112.pack()
    an113 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an113.insert(0, "")
    an113.pack()
    an114 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an114.insert(0, "")
    an114.pack()
    an115 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an115.insert(0, "")
    an115.pack()
    an116 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an116.insert(0, "")
    an116.pack()
    an117 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an117.insert(0, "")
    an117.pack()
    an118 = Entry(root,font=('calibre',font1,'bold'),width=20)
    an118.insert(0, "")
    an118.pack()
    # an119 = Entry(root,font=('calibre',font1,'normal'),width=25)
    # an119.insert(0, "")
    # an119.pack()
    # an120 = Entry(root,font=('calibre',font1,'normal'),width=25)
    # an120.insert(0, "")
    # an120.pack()

    an111.place(x=900,y=308)
    an112.place(x=900,y=338)
    an113.place(x=900,y=368)
    an114.place(x=900,y=398)
    an115.place(x=900,y=428)
    an116.place(x=900,y=458)
    an117.place(x=900,y=488)
    an118.place(x=900,y=518)


    # shirt4 = Label(text="x3R",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # pant4 = Label(text="p>3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # Tshirt4= Label(text="i3-x3R",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # nightpant4= Label(text="na{3p>3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # bermuda4= Label(text="brmoDa",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # underwear4= Label(text="A.DrveAr",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # baniyan4= Label(text="bnIyn",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    # salvar4= Label(text="slvar",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")

    # shirt4.place(x=900,y=308)
    # pant4.place(x=900,y=338)
    # Tshirt4.place(x=900,y=368)
    # nightpant4.place(x=900,y=398)
    # bermuda4.place(x=900,y=428)
    # underwear4.place(x=900,y=458)
    # baniyan4.place(x=900,y=488)
    # salvar4.place(x=900,y=518)

    discount4= Label(text="DISka].3",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
    ekun4= Label(text="0ku`",font=("Marathi-Lekhani", font1, 'bold'),background=background1,foreground="black")
   
    discount4.place(x=1140,y=548)
    ekun4.place(x=1150,y=578)
  
    #_______________nag , rupay entry____________________

    shirt3 = Entry(root,font=('calibre',14,'normal'),width=5)
    shirt3.insert(0, "0")
    shirt3.pack()
    shirt33 = Entry(root,font=('calibre',14,'normal'),width=5)
    shirt33.insert(0, "0")
    shirt33.pack()
    pant3 = Entry(root,font=('calibre',14,'normal'),width=5)
    pant3.insert(0, "0")
    pant3.pack()
    pant33 = Entry(root,font=('calibre',14,'normal'),width=5)
    pant33.insert(0, "0")
    pant33.pack()
    Tshirt3 = Entry(root,font=('calibre',14,'normal'),width=5)
    Tshirt3.insert(0, "0")
    Tshirt3.pack()
    Tshirt33 = Entry(root,font=('calibre',14,'normal'),width=5)
    Tshirt33.insert(0, "0")
    Tshirt33.pack()
    nightpant3 = Entry(root, font=('calibre',14,'normal'),width=5)
    nightpant3.insert(0, "0")
    nightpant3.pack()
    nightpant33 = Entry(root, font=('calibre',14,'normal'),width=5)
    nightpant33.insert(0, "0")
    nightpant33.pack()
    bermuda3 = Entry(root,font=('calibre',14,'normal'),width=5)
    bermuda3.insert(0, "0")
    bermuda3.pack()
    bermuda33 = Entry(root, font=('calibre',14,'normal'),width=5)
    bermuda33.insert(0, "0")
    bermuda33.pack()
    underwear3 = Entry(root,font=('calibre',14,'normal'),width=5)
    underwear3.insert(0, "0")
    underwear3.pack()
    underwear33 = Entry(root, font=('calibre',14,'normal'),width=5)
    underwear33.insert(0, "0")
    underwear33.pack()
    baniyan3 = Entry(root,font=('calibre',14,'normal'),width=5)
    baniyan3.insert(0, "0")
    baniyan3.pack()
    baniyan33 = Entry(root, font=('calibre',14,'normal'),width=5)
    baniyan33.insert(0, "0")
    baniyan33.pack()
    salvar3 = Entry(root,font=('calibre',14,'normal'),width=5)
    salvar3.insert(0, "0")
    salvar3.pack()
    salvar33 = Entry(root, font=('calibre',14,'normal'),width=5)
    salvar33.insert(0, "0")
    salvar33.pack()
    discount33 = Entry(root, font=('calibre',14,'normal'),width=5)
    discount33.insert(0, "0")
    discount33.pack()

    # shirt333 = Entry(root,font=('calibre',14,'normal'),width=5)
    # shirt333.insert(0, "0")
    # shirt333.pack()
    # pant333 = Entry(root,font=('calibre',14,'normal'),width=5)
    # pant333.insert(0, "0")
    # pant333.pack()
    # Tshirt333 = Entry(root,font=('calibre',14,'normal'),width=5)
    # Tshirt333.insert(0, "0")
    # Tshirt333.pack()
    # nightpant333 = Entry(root, font=('calibre',14,'normal'),width=5)
    # nightpant333.insert(0, "0")
    # nightpant333.pack()
    # bermuda333 = Entry(root, font=('calibre',14,'normal'),width=5)
    # bermuda333.insert(0, "0")
    # bermuda333.pack()
    # underwear333 = Entry(root, font=('calibre',14,'normal'),width=5)
    # underwear333.insert(0, "0")
    # underwear333.pack()
    # baniyan333 = Entry(root, font=('calibre',14,'normal'),width=5)
    # baniyan333.insert(0, "0")
    # baniyan333.pack()
    # salvar333 = Entry(root, font=('calibre',14,'normal'),width=5)
    # salvar333.insert(0, "0")
    # salvar333.pack()

    shirt3.place(x=1104.5,y=307)
    shirt33.place(x=1168,y=307)
    pant3.place(x=1104.5,y=337)
    pant33.place(x=1168,y=337)
    Tshirt3.place(x=1104.5,y=367)
    Tshirt33.place(x=1168,y=367)
    nightpant3.place(x=1104.5,y=397)
    nightpant33.place(x=1168,y=397)
    bermuda3.place(x=1104.5,y=427)
    bermuda33.place(x=1168,y=427)
    underwear3.place(x=1104.5,y=457)
    underwear33.place(x=1168,y=457)
    baniyan3.place(x=1104.5,y=487)
    baniyan33.place(x=1168,y=487)
    salvar3.place(x=1104.5,y=517)
    salvar33.place(x=1168,y=517)
    discount33.place(x=1230.5,y=547)

    # shirt333.place(x=1230.5,y=307)
    # pant333.place(x=1230.5,y=337)
    # Tshirt333.place(x=1230.5,y=367)
    # nightpant333.place(x=1230.5,y=397)
    # bermuda333.place(x=1230.5,y=427)
    # underwear333.place(x=1230.5,y=457)
    # baniyan333.place(x=1230.5,y=487)
    # salvar333.place(x=1230.5,y=517)

    button3 = Button(root, text = "Save",style = 'W.TButton',command = total1)
    button3.place(x=1180,y=635)

#________________________________________________________________________________________________________________


#___________date ___________
x = datetime.datetime.now()
date1=x.strftime("%d/%m/%Y")
print(date1)

#________root__________________
root=Tk()
root.geometry('1366x728')
root.title('Mahalakshmi')
background1='white'
background2="grey50"
font=15
font1=12

root.configure(background=background1)

style1 = Style()
style1.configure('W.TButton', font = ('calibri', 15, 'bold'),background=background2, foreground = 'black')

style2 = Style()
style2.configure('E.TButton', font = ('calibri', 12, 'bold'),background=background2, foreground = 'black')

spath = "abc.jpeg"
simg = ImageTk.PhotoImage(Image.open(spath))
my = Label(root,image=simg)
my.image = simg


Login_A = Canvas(root, bg ="white", height = 230, width = 410,relief=FLAT) 
Login_A.place(x=920,y=20)
name_var =StringVar() 
passw_var = StringVar()
name_label = Label(root, text = 'Username', font=('calibre', 15, 'bold'),background="white", foreground = 'black') 
name_entry = Entry(root, textvariable = name_var,font=('calibre',15,'normal'))
passw_label = Label(root,text = 'Password', font = ('calibre',15,'bold'),background="white", foreground = 'black')
passw_entry= Entry(root, textvariable = passw_var, font = ('calibre',15,'normal'), show = '*') 
login_fail = Label(root, text = 'Invalid Username or Password', font=('calibre', 10, 'bold'),
    background="white", foreground = 'Red')
login_button = Button(root, text = "Login",style = 'W.TButton',command = login)


# main_title3 = Label(text="mhal(mI ",font=("Marathi-Lekhani", 60, 'bold'),background=background1,foreground="red")
# main_title4 = Label(text="TOP SHOP",font=("calibri", 30, 'bold'),background=background1,foreground="red")
# main_title5 = Label(text="re.da; ",font=("Marathi-Lekhani", 32, 'bold'),background=background1,foreground="red")

# button1 = Button(root, text = "Measurement",style = 'W.TButton',command = canvas_excel_1)
# button2 = Button(root, text = "Bill",style = 'W.TButton',command = canvas_excel_2)
# # button3 = Button(root, text = "third",style = 'W.TButton',command = Measurements1)

main()
root.mainloop()
