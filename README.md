> **Warning**
> 
> No Longer maintaining it, you can check out the Go version [here](https://github.com/musaubrian/tinygo)



# MyTinyDB 🗃️

> **Simple password generator and database that uses the ***tinyDB*** module**

## Setup

**Clone the repo**

```
git clone https://github.com/musaubrian/myTinyDB tiny_db
```

```sh
cd tiny_db
```

run **set-up.py**

**_linux_**

```sh
./set-up.py
Collecting tinydb==4.5.2
  Downloading tinydb-4.5.2-py3-none-any.whl (23 kB)
Installing collected packages: tinydb
Successfully installed tinydb-4.5.2
=================
Everything is set
```

---

### Run the script:

**_linux_**

```sh
./main.py
```

## a) Password Generator

Clears the screen and saves the password to the clipboard

```sh
****************************************

        what shall it be today?
            database: db
        password generator: gen

****************************************


~# gen


password copied to clipboard
****************************

```

## b) Database

### 1. Adding user and related content

Sites are added without the extension for easier searching
**example:**

- github.com ❌
- github or Github ✔

Enter **a** to the prompt

```
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ a
```

It will prompt you to select
whether you want to insert **mutliple inputs`m`** or just a single **input `s`**

```
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ a
Multpile or Single input(m/s)
~$
```

It exits automatically

### 2. Searching for user and related information

**_Currently only searches by site name_**

Input `s` into the prompt to enter search mode.

Enter **sitename**

```
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ s
**************************************
🔍Searches for Sites and related info
**************************************
Enter sitename: example

```

### 3. Delete user and related content

Enter **d** to enter delete mode

Enter user to delete

```
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ d
*********************************
Deletes user and related info 💀
*********************************
Enter username: testUser
```

### 4. Show-all users and related information

Shows all the user
Input `sh`

```
***********************************************

                  TinyDB🗃️
➕ Add / 🔍 Search / ❌ Delete / 👀 Show-all
              (𝗮 / 𝘀 / 𝗱 / 𝘀𝗵)

***********************************************

~$ sh

```
