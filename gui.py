import tkinter as tk

# import filedialog module
from tkinter import filedialog

if __name__ != '__main__':
    func = function  # passed object


def str_to_list(in_str):
    return list(map(int, in_str.split(',')))


def add_component(win):
    uic, frames = {}, {}
    tmp_uic = {}

    #################
    # Constants
    ent_width = 10
    frm_padx = 10
    frm_pady = 3

    #####################################
    # Event handler

    def browse_click_run():
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(("CSV (Comma delimited)",
                                                          "*.csv*"),
                                                         ("all files",
                                                          "*.*")))
        # Change label contents
        func(filename)

    ##################################################################################################################
    # UI

    tmp_uic['btn_browse'] = tk.Button(
        win,
        text="Browse",
        width=20,
        height=20,
        command=browse_click_run
    )
    # tmp_uic['btn_1'].bind("<Button-1>", handle_click_run) # if you want pass event to function

    [i.pack(side=tk.TOP, padx=frm_padx, pady=10 * frm_pady) for i in tmp_uic.values()]
    uic.update(tmp_uic)

    return uic


# Main window running

window = tk.Tk()
window.title("Flat Defined Tree to Child ID")
window.geometry("330x100")
window.config(bg="Gray")

comp = add_component(window)

# show GUI
window.mainloop()
