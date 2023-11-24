# Coders Parkhouse

Coders Parkhouse is a Python Terminal Application which should simulate a real life situation of using a parking lot. There is a little twist to it, to make it a little bit more entertaining.

[Coders Parkhouse live project here.](https://coders-parkhouse-e4a324d9bf40.herokuapp.com/)

![Am I Responsive](assets/images/mockup-image-coders-parkhouse.png)

## **Table of Content**

### [**User Experience (UX)**](#user-experience-ux-aa)

- [User Stories](#user-stories)

### [**Flowcharts**](#flowcharts)

### [**Features**](#features-aa)

- [Welcome to Coders Parkhouse](#welcome-to-coders-parkhouse)
- [Park the car](#park-the-car)
- [Entering Registration Number](#entering-registration-number)
- [Paying Debt/Actually Mistake](#paying-debtactually-mistake)
- [Parking Duration(Hours)](#parking-durationhours)
- [Return/NotYet](#returnnotyet)
- [Leave Parking Lot](#leave-parking-lot)
- [Parking Details](#parking-details)
- [Time of Arrival](#time-of-arrival)
- [Discount Code](#discount-code)
- [Pay at Exit](#pay-at-exit)
- [Further Improvements](#further-improvements)

### [**Technologies Used**](#technologies-used-aa)

- [Languages](#languages)
- [Libraries](#libraries)
- [Frameworks and Other Programs](#frameworks-and-other-programs)

### [**Testing**](#testing-aa)

- [Validation Results](#validation-results)
- [Manual Testing](#manual-testing)
- [Fixed Bugs](#fixed-bugs)
- [Knows Bugs](#known-bugs)

### [**Deployment and local development**](#deployment-and-local-development-aa)

- [Deploying to Heroku](#deploying-to-heroku)
- [Forking the GitHub Repository](#forking-the-github-repository)

### [**Credits**](#credits-aa)

- [Content](#content)
- [Media](#media)

## <a id="user-experience-ux-aa"></a>**User Experience (UX)**

Using of this application is pretty straight forward as it would be to use parking lot services in real life. Driver/User is greeted with the ASCII art at the entrance letting the driver know where he is.

### **User Stories**

- **User/Driver goals**

  - Be able to enter/leave parking lot.
  - Be able to see the prices at the entrance.
  - Be able to park for cheap price.
  - Be able to use automated parking system.
  - Be able to understand instructions easily.
  - Be able to enter registration into predetermined template.
  - Be able to know time(duration) of parking.
  - Be able to know total cost of the parking.
  - Be able to get some discount. :)

- **Creator/Owner goals**

  - Present own services in understandable manner.
  - Instuctions to be intuitive.
  - Handle possible invalid inputs from customers.
  - Prices to be competitive.
  - Offer to the user to reject if he isn't satisfied with the prices.
  - Track the time spent on the parking lot.
  - Calculating the price automatically according to the time spent.
  - Have the track of the cars on the lot.
  - Have the track of previous debts of certain cars(imaginary).
  - Be kind to the customers.
  - Be able to offer small discount to the customers.

## <a id="flowcharts"></a>**Flowcharts**

- **Initial Flowcharts**

  - Flowcharts used as a base for development process.
    <details>
    <summary>Initial Flowcharts
    </summary>

    ![Initial Flowcharts](/assets/images/flowcharts/coders-parkhouse-flow-diagram.png)
    </details>

- **Final Flowcharts**

  - Flowcharts after all desired functions were implemented.
    <details>
    <summary>Final Flowcharts
    </summary>

    ![Final Flowcharts](/assets/images/flowcharts/coders-parkhouse-flow-diagram-improved.png)
    </details>

## <a id="features-aa"></a>**Features**

When you go to [Coders Parkhouse](https://coders-parkhouse-e4a324d9bf40.herokuapp.com/), this is what is waiting for you.

### **Welcome to Coders Parkhouse**

At the entrance/exit you are being greeted and two options are being given to you:
  1. To park the car.
  2. To leave the parking lot.
  - ![Entrance/Exit](/assets/images/features/feature1-welcome.png)

### **Park the car**

- If you choose to park the car, the rules of the parking house are being displayed to you. You are also being asked if you accept to the terms of use, which you can accept or reject and search for a better place to park.
- ![Rules](/assets/images/features/feature2-rules.png)

- If you reject the terms of use, you will be greeted nicely.
- ![Rules No](/assets/images/features/feature3-rules-no.png)

- If you accept and you do want to park here, you will be taken to the next step.
- ![Rules Yes](/assets/images/features/feature4-rules-yes-regplate-entry.png)

### **Entering Registration Number**

- Here you must enter your registration number but according to one of the four given patterns. Instructions are telling you to use letters, digits and dashes only, other characters will trigger Invalid Input.

- In case you use valid pattern for your registration number, you can have 2 scenarios:
  1. You type in valid registration number and you can go further to enter the parking duration.
  - ![Regplates Valid Not Existing](/assets/images/features/feature5-regplates-valid-not-existing-hours.png)


  2. You type in valid registration number, but you find out there is a debt from the last time, which you need to take care of, so that you can park here again. Behind the scenes the code is checking if the given registration is already inside the google sheet. In this case it is which represents your "debt".
  - ![Regplates Valid Existing](/assets/images/features/feature8-regplate-existing.png)

### **Paying Debt/Actually Mistake**

- You have 2 options here to pay your debt, to be able to park again or to type in your registration number again because actually it was a typo.

  1. If you choose to pay your debt, after the transaction is over, you will be able to enter your registration number again and park as you wish. In reality the reg. number is getting deleted from the google sheet, so you are able to enter with the same registration again.
  - ![Regplates Valid Existing Paying](/assets/images/features/feature10-regplates-existing-pay.png)

  2. If you actually made a mistake and you choose "new". You will be taken back to enter your registration number again.
  - ![Regplates Valid Existing New](/assets/images/features/feature9-regplate-existing-no.png)

### **Parking Duration(Hours)**

- ![Regplates Valid Hours](/assets/images/features/feature5-regplates-valid-not-existing-hours.png)
- When we manage to pay off our dept (^.-) and we enter the valid reg. number, we need to enter number of hours or let's say duration of our parking. In this case the number is unlimited.
- ![Hours Info](/assets/images/features/feature6-hours-info.png)

- In the background there is a list in program which holds the registration number, number of hours and price which is calculated according to the hours we enter.
- Price is calculated as: Hours * 3euro
- At this moment the list is being inserted into the google sheet.
- In this step the info about our parking is being presented to us.

### **Return/NotYet**

- After we are presented with the info in the end, we have two options:

  1. To leave, in this case we are typing in "not yet".
  - ![Not Yet](/assets/images/features/feature11-not-yet.png)

  2. Second option is to type in "return", to get back to the parking lot to pick up our car. It brings us to the beginning of our application.
  - ![Return](/assets/images/features/feature12-return.png)

### **Leave Parking Lot**

- After we come back to pick up our car, either by entering "return" at the end of our parking process or by restarting the program and we choose the option number two, to leave the parking lot, we need to enter our registrations again.
- By entering our reg. number again, the system is checking if the reg. number is in the google sheet(did we park here at all).

- ![Leaveing Parking Lot](/assets/images/features/feature13-regplatesleave.png)

- Here we are going to have 2 options.
- First one where the registration number is valid but car is not parked at our parking lot(not present in the google sheet).
- Second option, where registration number is valid and is parked at our parking lot(is present in the google sheet).

  - **Registration Not Existing**
  - ![Registration Not Existing](/assets/images/features/feature20-valid-regplateleave-not-existing.png)
  - Here we have 2 scenarios again, where the driver will be able to type in again the reg. number in case he made a typo or he can freely walk away in case he missed the parking lot(^_^).

    - Re-enter the registration number
      - I you type in "yes".
      - ![Re-enter Reg Number](/assets/images/features/feature22-regplates-not-existing-yes.png)

    - Walk away
      - If you type in "no".
      - ![Walk Away](/assets/images/features/feature21-regplates-not-existing-no.png)
  
  - **Registration Existing**
    - This will lead to details being loaded(we are loading info from the google sheet).
    - ![Registration Existing](/assets/images/features/feature24.png)


### **Parking Details**

- ![Details Loading](/assets/images/features/feature14-details-loading.png)

- When we enter registration number which is present in our system, we are getting full initial details about our parking.
- In the background the system is reading from the google sheet and pulling the row according to the registration number.
- After that we can choose between three possible scenarios, which represent our time of arrival.

### **Time of Arrival**

- According to the option we choose here, our price will be calculated. Meaning if we choose Earlier or On Point the price will actually be the same as the initial one, while if we choose Later, a fee of 10€ will be added to the initial price(the price here is calculated accodring to our parking rules).

- **Earlier/On Point**
  
- ![Earlier/On Point](/assets/images/features/feature15-1.png)

- **Later**

- ![Later](/assets/images/features/feature16-3.png)

### **Discount Code**

- Suddenly the driver will be asked if he knows about the CI discount code, to get 10% off of the final price.

- Here we will have two scenarios, where driver will know the code or he wouldn't. The Driver will be answered in a funny manner, according to the scenario.

  - **With Code**
  - ![With Code](/assets/images/features/feature23.png)

  - **No Code**
  - ![No Code](/assets/images/features/feature17-no-code.png)

### **Pay at Exit**

- In the end, we are prompted to pay the final price we got.
- There will be 2 scenarios again, where we can choose between "pay" or anything else.
- In order to exit the parking lot, we must choose "pay" in the end.

  - **Not Wanting to Pay**
  - ![Not Paying](/assets/images/features/feature19-leave-no-pay.png)

  - **Pay**
  - ![Paying](/assets/images/features/feature18-leave-paying.png)

  - After we pay, we are greeted again and we can freely exit the parking lot.
  - In this step program is deleting the info from our google sheet.

### **Further Improvements**

- Add coloring for Valid/Invalid inputs, green/red for example, for better UX(lack of time).
- Improve system to track time automatically, which will eleminate need of the given 3 scenarios(earlie, on point, late).
- Improve parking system to track real date/time(real life application).
- Improve pricing system in case people want to leave their cars for a longer period of time and ajust prices. Maybe give some better options for those who want to park for a longer period(days, weeks...), since at the moment this option is simple number of hours and is unlimited(real life application).
- Add cameras to replace manual input of registration number(real life application).
- Add printer which will print out cards with the registration number, time and date. Those cards would be needed at the exit, at the payment process(real life application).

## <a id="technologies-used-aa"></a>**Technologies Used**

### **Languages**

- Python
- JavaScript (used by template creator)
- HTML (used by template creator)

### **Libraries**

- [gspread](https://github.com/burnash/gspread)
  - Google API for GoogleSheets.
- [google.oauth2.service_account](https://developers.google.com/identity/protocols/oauth2/service-account)
  - System used for server-to-server interactions.
- [regex](https://docs.python.org/3/howto/regex.html)
  - Regular Expression used for setting up patterns.

### **Frameworks and Other Programs**

- [Git](https://git-scm.com/)
   - Used for version control, commit to Git and Push to GitHub.
- [GitHub](https://github.com/)
   - Used to store the code online and for deployment.
- [Gitpod](https://www.gitpod.io/)
   - Used for development as a cloud IDE.
- [Heroku](https://id.heroku.com/login)
  - Used to deploy the project.
- [drawio](https://www.drawio.com/)
  - Used to create Flowcharts.
- [PEP8CI - Python Linter](https://pep8ci.herokuapp.com/)
  - Used to validate Python code.
- [Am I Responsive](https://ui.dev/amiresponsive)
   - Used to create mockup image for the README file.
- [Text to ASCII Art Generator](https://www.patorjk.com/software/taag/#p=display&f=Broadway%20KB&t=Coders%20Parkhouse)
  - Used to create ASCII art for welcoming and farewell messages.

## <a id="testing-aa"></a>**Testing**

Software used to validate the Pythone code is PEP8CI - Python Linter, mentioned in the Frameworks and Other Programs section above.

### **Validation Results**

  - Before:
    <details>
    <summary>Linter Errors 1
    </summary>
    
    ![Linter Errors 1](/assets/images/bugs/linter-errors-1.png)
    </details>

    <details>
    <summary>Linter Errors 2
    </summary>
    
    ![Linter Errors 2](/assets/images/bugs/linter-errors-2.png)
    </details>

  - After:
      <details>
      <summary>Linter No Errors
      </summary>
      
      ![Linter No Errors](/assets/images/bugs/linter-all-good.png)
      </details>

### **Manual Testing**

<table>
<thead>
  <tr>
    <th>Feature</th>
    <th>User Input/State</th>
    <th>Output</th>
    <th>Result</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Application Loads</td>
    <td>No Input</td>
    <td>Welcoming menu is presented.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Welcoming Options</td>
    <td>1</td>
    <td>Driver chooses to park.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Welcoming Options</td>
    <td>2</td>
    <td>Driver chooses to leave.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Welcoming Options</td>
    <td>3</td>
    <td>That's not an option!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Welcoming Options</td>
    <td>#</td>
    <td>You must choose between numbers 1 and 2.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Welcoming Options</td>
    <td>Any special character</td>
    <td>You must choose between numbers 1 and 2.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Parking Rules</td>
    <td>yes</td>
    <td>Proceeds to registration entry.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Parking Rules</td>
    <td>no</td>
    <td>Farewell message</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Parking Rules</td>
    <td>1</td>
    <td>Please answer with yes or no.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Parking Rules</td>
    <td>#</td>
    <td>Please answer with yes or no.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Parking Rules</td>
    <td>Empty space</td>
    <td>Please answer with yes or no.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Parking Rules</td>
    <td>Any special character</td>
    <td>Please answer with yes or no.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY-123-XY</td>
    <td>Reg. number is valid.(if not in system already)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY-1234-XY</td>
    <td>Reg. number is valid.(if not in system already)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XYZ-123-XY</td>
    <td>Reg. number is valid.(if not in system already)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XYZ-1234-XY</td>
    <td>Reg. number is valid.(if not in system already)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY-123-XY</td>
    <td>Reg. number is already in our system!(if it is present in the system aleady)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY-1234-XY</td>
    <td>Reg. number is already in our system!(if it is present in the system aleady)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XYZ-123-XY</td>
    <td>Reg. number is already in our system!(if it is present in the system aleady)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XYZ-1234-XY</td>
    <td>Reg. number is already in our system!(if it is present in the system aleady)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY-12345-XY</td>
    <td>Please use one of the given patterns.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XYZABC-12345-ZZXY</td>
    <td>Please use one of the given patterns.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY- 1 2 3-XY</td>
    <td>Please use one of the given patterns.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>123-123-123</td>
    <td>Sorry, Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>#</td>
    <td>Sorry, Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>Empty space</td>
    <td>Sorry, Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input</td>
    <td>XY-123-XY!^$@</td>
    <td>Sorry, Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay Debt/ New</td>
    <td>pay</td>
    <td>Paying...Ok now you can park here again.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay Debt/ New</td>
    <td>new</td>
    <td>Back to Registration Number Input.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay Debt/ New</td>
    <td>no</td>
    <td>Invalid Input! Sorry but "no" is not an option!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay Debt/ New</td>
    <td>#</td>
    <td>Invalid Input! Sorry but "#" is not an option!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay Debt/ New</td>
    <td>new1</td>
    <td>Invalid Input! Sorry but "new1" is not an option!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay Debt/ New</td>
    <td>Empty space</td>
    <td>Invalid Input! Sorry but " " is not an option!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>0</td>
    <td>Zero is not an option, sorry.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>0.2</td>
    <td>Use only didigts 0-9, only whole numbers please. No special signs neither.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>#</td>
    <td>Use only didigts 0-9, only whole numbers please. No special signs neither.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>!</td>
    <td>Use only didigts 0-9, only whole numbers please. No special signs neither.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>Empty space</td>
    <td>Use only didigts 0-9, only whole numbers please. No special signs neither.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>Any special character</td>
    <td>Use only didigts 0-9, only whole numbers please. No special signs neither.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>python</td>
    <td>Use only didigts 0-9, only whole numbers please. No special signs neither.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>1</td>
    <td>Very well! Try not to be late, otherwise it will be more expensive.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>5</td>
    <td>Very well! Try not to be late, otherwise it will be more expensive.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Number of Hours</td>
    <td>999</td>
    <td>Very well! Try not to be late, otherwise it will be more expensive.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>#</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>Empty space</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>1</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>mama</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>Any special character</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>return_</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>return</td>
    <td>Welcoming menu is presented.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Return/Not Yet</td>
    <td>not yet</td>
    <td>Ok, see ya later!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>Empty space</td>
    <td>Invalid data, please use correct pattern.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>123</td>
    <td>Invalid data, please use correct pattern.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>#</td>
    <td>Invalid data, please use correct pattern.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>Any special character</td>
    <td>Invalid data, please use correct pattern.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>XY-__123__-XY</td>
    <td>Invalid data, please use correct pattern.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>XY-123-XY</td>
    <td>Registration number is valid but not in our system. Are you sure that you parked here?(if not present in the system)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>XYZ-1234-XY</td>
    <td>Registration number is valid but not in our system. Are you sure that you parked here?(if not present in the system)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>XYZ-1234-XY</td>
    <td>Valid Input! Details loading...(if reg. number is present in the system)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Input / Leaving parking lot</td>
    <td>AA-123-BC</td>
    <td>Valid Input! Details loading...(if reg. number is present in the system)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>!</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>#</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>123</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>Any special character</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>!yes</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>No%</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>+yes</td>
    <td>Please answer with "yes" or "no".</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>yes</td>
    <td>We need your registration number please.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Reg. Number Valid but not in system.(Yes/No)</td>
    <td>no</td>
    <td>Have a nice day! Until the next time!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>#</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>4</td>
    <td>That's not an option.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>0.5</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>Empty space</td>
    <td>Invalid Input!</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>-1</td>
    <td>That's not an option.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>+1</td>
    <td>Don't use prefix plus.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>1</td>
    <td>Your final price should be X€.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>2</td>
    <td>Your final price should be X€.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Time of arrival (Options: 1, 2 or 3)</td>
    <td>3</td>
    <td>Your final price should be X€.</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Discount Code</td>
    <td>123</td>
    <td>Looks like your boss doesn't like you so much. :(</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Discount Code</td>
    <td>#</td>
    <td>Looks like your boss doesn't like you so much. :(</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Discount Code</td>
    <td>Empty space</td>
    <td>Looks like your boss doesn't like you so much. :(</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Discount Code</td>
    <td>Any special character</td>
    <td>Looks like your boss doesn't like you so much. :(</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Discount Code</td>
    <td>CI2023/ci2023</td>
    <td>Looks like your boss likes you. :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>0</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>#</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>Empty space</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>Empty space + "pay"</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>pay_</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>pay+</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>Any special character</td>
    <td>Sorry, until you pay, you can't drive out! :)</td>
    <td>Confirmed</td>
  </tr>
  <tr>
    <td>Pay at Exit</td>
    <td>pay</td>
    <td>Paying...Complete! Have a nice day! Until next time!</td>
    <td>Confirmed</td>
  </tr>
</tbody>
</table>

### **Fixed Bugs**

- **Bug 1:**

  - Multiple lists written into the google sheet, after the driver would "return" and use same registration in the registration input section, after paying the debt off.

    <details>
    <summary>Bug 1 Image
    </summary>
        
    ![Linter No Errors](/assets/images/bugs/bug-before-clearing-the-list.png)
    </details>

- **Fix 1:**

  - This was sorted with clear() method on the list which holds the driver details, before "return" part of the application.

    <details>
    <summary>Fix 1 Image
    </summary>
          
    ![Linter No Errors](/assets/images/bugs/list-cleared.png)
    </details>

- **Bug 2:**

  - In the Time of Arrival part of program, when user has to choose between options Earlier, On Point and Later, by inputing 1, 2, or 3. The program would accept multiple empty spaces before and after 1, 2, or 3.

    <details>
    <summary>Bug 2 Image
    </summary>
          
    ![Linter No Errors](/assets/images/bugs/bug123.png)
    </details>

- **Fix 2:**

  - It was sorted out by using len() method on the real_duration string, and if statement insuring that it's lenght is not bigger than 1.

    <details>
    <summary>Fix 2 Image
    </summary>
          
    ![Linter No Errors](/assets/images/bugs/empty-spaces-solution.png)
    </details>

- **Bug 3:**

  - While entering the registration number in case of parking or leaving the parking lot, the program would accept registration as valid as long as it would contain the number of correct pattern even if before and after the registration number would be special characters.
  - For example: ###XY-123-XY%%% would be accepted, ___XYZ-1234-XY//.#@ would be accepted and so on...

    <details>
    <summary>Bug 3 Image
    </summary>
          
    ![Linter No Errors](/assets/images/bugs/crazy-pattern.png)
    </details>

- **Fix 3:**

  - This was fixed by adding the special characters for start and end of the pattern within the string, which represents my registration numbers pattern.('^---pattern---$')

    <details>
    <summary>Fix 3 Image
    </summary>
          
    ![Linter No Errors](/assets/images/bugs/pattern-solution.png)
    </details>

### **Known Bugs**

- At the moment there are no known bugs.

- The only thing I can mention is that terminal which runs the code on the Heroku, is not responsible. It means if we reduce the width of the browser the terminal will get covered. That has nothing to do with the project itself.

## <a id="deployment-and-local-development-aa"></a>**Deployment and local development**

###  **Deploying to Heroku**

1. Go to [Heroku](https://id.heroku.com/login), create account if you don't have and log in.

2. Head to your dashboard nad click "New", then "Create new app"

    <details>
    <summary>New/CreateNewApp
    </summary>
              
    ![New/CreateNewApp](/assets/images/deployment/step1-create-new-app.png)
    </details>

3. Next step is to give your app a name and to choose region. After that click on "Create app".

    <details>
    <summary>Name/Region/Create
    </summary>
              
    ![Name/Region/Create](/assets/images/deployment/step2.png)
    </details>

4. After that head to "Settings" tab which you can find in the header of your Heroku page and under the "Config Vars" set your Key/Value Pairs.

    <details>
    <summary>CREDS/PORT
    </summary>
              
    ![CREDS/PORT](/assets/images/deployment/step3.png)
    </details>

5. Then in the "Buildpacks" section you will need to add buildpacks. Pay attention to the order in which you add buildpacks you need. In my case I had to add Python first and nodejs second.

    <details>
    <summary>Buildpacks
    </summary>
              
    ![Buildpacks](/assets/images/deployment/step4.png)
    </details>

6. First add "Python", by clicking on Python icon and then click on "Add Buildpack".

    <details>
    <summary>Python
    </summary>
              
    ![Python](/assets/images/deployment/step5-python.png)
    </details>

7. Then add "nodejs", by clicking on nodejs icon and then click on "Add Buildpack".

    <details>
    <summary>nodejs
    </summary>
              
    ![nodejs](/assets/images/deployment/step6-nodejs.png)
    </details>

8. Then head to "Deployment" tab which you can also find in the header of your Heroku page and under "Deployment method" click on "GitHub"(in my case that's where my repository is).

    <details>
    <summary>GitHub
    </summary>
              
    ![GitHub](/assets/images/deployment/step7-github.png)
    </details>

9. After that, just under the "Deployment method" section is "Connect to GitHub" section where you need to find your repository and then click on "Connect".

    <details>
    <summary>Connect
    </summary>
              
    ![Connect](/assets/images/deployment/step8.png)
    </details>

10. Just under "Connect to GitHub" section is "Automatic deploys" section where you can click on "Enable Automatic Deploys" if that's what you want and just under is "Manual Deploy" section, where you need to click on "Deploy Manually".

    <details>
    <summary>EnableAutomaticDeploys/DeployManually
    </summary>
              
    ![EnableAutomaticDeploys/DeployManually](/assets/images/deployment/step9-deployment-type.png)
    </details>

### **Forking the GitHub Repository**

By forking the GitHub Repository we can make a copy of the original repository to view or make changes without changing the original repository.

1. Log in to GitHub and locate [Coders Parkhouse](https://github.com/AleksandarJavorovic/coders-parkhouse)
2. At the top, in the line with the project's name, on the right side find "Fork", click.
3. Now you have a copy of the original repository in your GitHub account.