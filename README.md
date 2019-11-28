# Sygnal 
Sygnal is a hybrid wireless network simulation

## Project containers

`core/` contains the core logic of the algorithms regarding route establishment and channel allocation

`client/` is a React app initiated with [CRA](https://create-react-app.dev) that controls the views of the app as a whole 

`server.py` is the initial backend core that uses `socket.io` to communicate with the client

## Development Setup

We will walkthrough how to setup the development environment

### Pre-Requirements

In order to start contributing, you will need `Node.js v10+` and `Python v3.6+`

### Packages
First, we'll need to install some packages to work with the app

<details>
  <summary>Linux</summary>
  In your **Debian** based linux distro, run the following
  ```bash
  $ sudo apt install python3-pip -y
  $ sudo pip3 install virtualenv
  ```
</details>

<details>
  <summary> macOS & Windows </summary>
  1. Install a VM Emulator from [VirtualBox](https://virtualbox.org)
  2. Then install and boot an Ubuntu (or any Debian) distro
  3. Run the above linux commands after installing the pre-requisite software
</details>

### Dependency Management

To make sure that you can run code without any clashes, intialize a `virtualenv` wrapper for Python. 

```bash
git clone https://github.com/f0cus10/sygnal	#Clone this repository
python3 -m venv .venv				#Initialize a virtualenv wrapper at .venv
source .venv/bin/activate			#Use the virtualenv Python executable
pip -r requirements.txt				#Install the dependencies for the backend
```

Next, we move to the client and setup the dependencies on the client side
```bash
cd client	#Move into the client directory
npm install	#Install all dependencies through npm
```

### Script

This is the final step, where you run the commands to start up the backend and front-end

***NOTE:*** For now, this has to be done in two different terminal windows as two separate commands. But this may change

To intialize the *backend* server, from the project root directory, run:
```bash
python server.py
```
Please make sure that you are running the Python executable from the virtualenv wrapper that you selected at [Dependency Management](#dependency-management)

Next, run the frontend in a different terminal:
```bash
cd client
npm start
```

Now, you can visit the URL of the frontend app to see your app in action!
*Remember* to check all your ports. It will usually be http://localhost:3000
