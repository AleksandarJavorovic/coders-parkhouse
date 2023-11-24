# Coders Parkhouse

Coders Parkhouse is a Python Terminal Application which should simulate a real life situation of using a parking lot. There is a little twist to it, to make it a little bit more entertaining.

[Coders Parkhouse live project here.](https://coders-parkhouse-e4a324d9bf40.herokuapp.com/)

![Am I Responsive](assets/images/mockup-image-coders-parkhouse.png)

## **Table of Content**

### [**User Experience (UX)**](#user-experience-ux-aa)

- [User Stories](#user-stories)

### [**Flowcharts**](#flowcharts)

### [**Features**](#features-aa)

### [**Technologies Used**](#technologies-used-aa)

- [Languages Used](#languages-used)
- [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)

### [**Testing**](#testing-aa)

- [Validation Results](#validation-results)
- [Manual Testing](#manual-testing)
- [Fixed Bugs](#fixed-bugs)
- [Knows Bugs](#known-bugs)

### [**Deployment and local development**](#deployment-and-local-development-aa)

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
  - Be able to get some discount in case he is an developer. :)

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

## **Flowcharts**

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

### **Parking Details, Time of Arrival**

- ![Details Loading](/assets/images/features/feature14-details-loading.png)

- When we enter registration number which is present in our system, we are getting full initial details about our parking.
- In the background the system is reading from the google sheet and pulling the row according to the registration number.
- After that we can choose between three possible scenarios, which represent our time of arrival.



