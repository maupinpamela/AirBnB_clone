# 0x00. AirBnB clone - The console
![Image of Holberton B&B Logo](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/263/HBTN-hbnb-Final.png)

### Description
This is an Airbnb Clone, the first part in a multipart project. In this part of the clone we used Python3 to build a command interpreter for the HBnB web app. The console is similar to the Simple Shell Project. There is a command line that will execute specific commands. The next steps for this project is to integrate HTLM/CSS, database storage, API and Front end web use.

### Environment
This function was developed and tested on `Ubuntu 14.04 LTS` via Vagrant in VirtualBox.

### File Contents
The repository contains the following files:

   **File**   |   **Description**
   -------------- | ---------------------
   AUTHORS | docker-formatted author file
   console.py | Launches the command interpreter
   base_model.py | functions to take care id the initialization, serialization and deserialization of the created instances
   city.py | Contains a public class attribute: name, state_id that inherits from BaseModel
   state.py | Contains a public class attribute: name that inherits from BaseModel
   amenity.py | Contains a public class attribute: name that inherits from BaseModel
   review.py | Contains a public class attribute: place_id, user_id, text that inherits from BaseModel
   place.py | Contains a public class attribute: city_id, user_id, name, description, number_rooms, number_bathrooms, max_guests, proce_by_night, latitude, longitude, amenity_ids that inherits from BaseModel
   user.py | Contains a public class attribute: email, password, first_name, last_name that inherits from BaseModel
   file_storage.py | contains the class FileStorage that serializes instances
to a JSON file and deserializes JSON files to instances
   README.md | readme file
   tests/ | contains the unittests for all methods

### Function Descriptions

 **Function** | **Description**
 -------------- | -----------------
 help | `help *[option]*` | Lists all available commands, or displays what option does
 quit | `quit` | Exit command interpreter
 EOF | `EOF` | Exit command interpreter
 create | `create [class_name]` or `[class_name].create()`| Creates an instance of class_name
 update | `update [class_name] [object_id] [update_key] [update_value]` or  `[class].update([object_id] [update_key] [update_value]()`| Updates the key:value of class_name.object_id instance
 show | `show [class_name] [object_id]` or `[class_name].show([object_id])()` | Displays all attributes of class_name.object_id
 all | `all [class_name]`, `[class_name].all()` | Displays every instance of class_name, if used without option displays every instance saved to the file
 destroy | `destroy [class_name] [object_id]` or `[class_name].destroy([object_id])()` | Deletes all attributes of class_name.object_id

### Usage and Installation
Clone the repository and then compile using gcc.
```
$ git clone git@github.com:AfaMadza/AirBnB_clone.git
```

###### Example command line call

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program
(hbnb) help EOF
Control D will exit program
(hbnb) create BaseModel
c601b0ad-adeb-4df6-9e40-c60b40b385b7
(hbnb) show BaseModel c601b0ad-adeb-4df6-9e40-c60b40b385b7
[BaseModel] (c601b0ad-adeb-4df6-9e40-c60b40b385b7) {'updated_at': datetime.datetime(20
18, 6, 14, 1, 16, 55, 551272), 'created_at': datetime.datetime(2018, 6, 14, 1, 16, 55,
 551240), 'id': 'c601b0ad-adeb-4df6-9e40-c60b40b385b7'}
(hbnb) destroy BaseModel c601b0ad-adeb-4df6-9e40-c60b40b385b7
(hbnb) show BaseModel c601b0ad-adeb-4df6-9e40-c60b40b385b7
** no instance found **
(hbnb) quit
```


---

### Authors

This project was created by:

* [**Afa Madza**](https://github.com/AfaMadza)
* [**Pamela Maupin**](https://github.com/maupinpamela)

<p align="center">
<a href="https://www.holbertonschool.com"><img src="https://intranet.hbtn.io/assets/holberton-logo-simplified-d4e8a1e8bf5ad93c8c3ce32895b4b53749b477b7ba7342d7f064e6883bcd3be2.png"></a>
</p>