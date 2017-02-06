# Alexa Monzo [![Build Status](https://travis-ci.org/danbondd/alexa-monzo.svg?branch=master)](https://travis-ci.org/danbondd/alexa-monzo)

An unofficial Alexa Skill for interacting with the Monzo API.

_**Prerequisites:** This application requires an [AWS](http://aws.amazon.com) account and a [Monzo](https://monzo.com) account._

## Installation

**Monzo OAuth Client**

- Create a [Monzo OAuth Client](https://developers.getmondo.co.uk/apps/home) and make a note of the `client_id` and `client_secret`.

**Lambda**
- Clone repository to your local machine and run the `make venv` command to configure your environment.
- Once you have a working `virtualenv`, run the `make zip` command to create the `lambda.zip` file.
- Sign in to your [AWS](https://aws.amazon.com) account and create a Lambda function for a [custom Alexa Skill](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/developing-an-alexa-skill-as-a-lambda-function).
    - Python 2.7
    - Upload the `lambda.zip` file created in step one.
    - Create an `ACCOUNT_ID` environment variable and set it to the Owner ID value provided in your [Monzo OAuth Client](https://developers.getmondo.co.uk/apps/home).
    - Create an `APP_ID` environment variable - _leave this blank, we'll come back to it later_.
    - Configure any other application properties (role, description, etc) to your liking.
    - Make a note of the `ARN`

**Alexa Application**

- Sign in to your [Amazon Developer](https://developer.amazon.com/) account and create a new Alexa Skills Kit.
- Configure the name and invocation name to your liking.
- Copy the Intent Schema, Custom Slot Types and Utterances from the `alexa-monzo` application `schema` folder.
- Under Configuration, set the following properties as outlined below:
    - Service Endpoint Type: AWS Lambda ARN (insert your Lambda ARN as noted earlier).
    - Account Linking: Yes
    - Authorization URL: https://auth.getmondo.co.uk/
    - Client Id: Your Monzo OAuth Client ID
    - Authorization Grant Type: Auth Code Grant
    - Access Token URI: https://api.monzo.com/oauth2/token
    - Client Secret: Your Monzo OAuth Client Secret.
- Configure any other required properties and enable your Alexa skill for testing.
- Once you have successfully created your Alexa Application, note the Application ID and update the `APP_ID` environment variable in your Lambda.

**Enable Alexa Skill**

- Sign in to the [Alexa web interface](http://alexa.amazon.co.uk/), enable your new skill and link your Monzo account - _note: this will **NOT** work in the mobile application, only the web interface._
 
Once the above steps are completed, you should be good to go!

## Usage

To see all accepted phrases, visit the `schema/utterances.txt` file.

- Balance
    - `Alexa, ask Monzo what my balance is.`
    - `Alexa, ask Monzo how much I've spent today.`

- Transactions
    - `Alexa, ask Monzo how much I've spent in the last 7 days.`
    - `Alexa, ask Monzo how much I've spent on transport in the last month.`

- Card
    - `Alexa, ask Monzo what my card status is.`
    - `Alexa, ask Monzo to block my card.`
    - `Alexa, ask Monzo to unblock my card.`
