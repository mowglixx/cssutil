# :ribbon: CSSUtil :ribbon:
 :ok_hand: An *OK* Utility Class CSS generator written in Python (3) 

## Words From The Author
>NGL, it's basically a ripoff of tailwind, I made this to see if I could make a script that spat out a css sheet with a bunch of *colours* *like* Tailwind, as I was making this I was like...
> 
>*"I could do with some padding and flexbox classes too..."*
>
> At the time of writing this bit here... The current line count of `main.css` when you run the defaults is **4478** lines of CSS vs **317** lines of Python, I have no life all I know is `hsl()` and a bunch of loops and now I *kinda* get flexbox... HELP, my head hurts.

## What works?
Have a look at the [Class List](class_list.md)

### Todo
- Finish flex classes
- fine-tune padding
- rounding
- other stuff idk

## How do?

Run the following command

```sh
# run in folder
python ./cssutil.py
```

### OK... but, What do?

The script will ask for a filename and will produce a `css` file and a `min.css` version in the **current folder**, the default filename is `main.css`. The output would be:
```sh
# files as below
./cssutil.py
./main.css
./main.min.css
```
#### Rules
- ~~The script *will* work with any old path~~
- The script *will* work with an *existing* path defined
- The script will output `<filename>.css` and a `<filename>.min.css`

If, for example, you defined `css/main.css` as the filename, as long as the `css` folder exists, the script should *just work:tm:* and output the files like this:

```sh
# files as below
./css/main.css
./css/main.min.css
./cssutil.py
```
If the folder doesn't exist, the script won't work, make the folder and try again, it's not a god.