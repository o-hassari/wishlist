A Step-By-Step Guide to OAuth 2.0: Implementing Sign In with Google, Facebook, and GitHub
#
webdev
#
javascript
#
programming
#
facebook
Introduction: What is OAuth 2.0 and How Does it Work?
OAuth is simply an open standard for token-based authorization that makes it easier for users to sign into your web app without having to create a new account each time. For example, if you're building a blog app, a new user of the app would normally have to create an account manually by filling out a form with a username, email and password. However, if you use OAuth instead, the user can log in with their existing Facebook, Google or GitHub account. This not only saves the user time but also helps reduce the number of abandoned accounts on your app.

For example, when we log in with Google, we are making a GET request to Google asking for the user's details. Google then responds with a POST request that includes the user's information. When it comes to authentication and security, another great benefit is that we can trust companies like Facebook and Google to manage passwords securely. These companies are known for having great engineers and teams who can provide the highest level of security.

As a developer, we can implement hashing, and salting to further increase password security using complex mathematical functions; however, it would take a considerable amount of time and effort for an individual or a small team. So why not we just delegate these tasks to large companies like Facebook and Google? Then, every time users log in to our app, we simply ask them to log in on Facebook and Facebook will then authenticate them using their security methods. After that, Facebook sends us the message saying this user is authenticated, they're a real Facebook user, and they've got the correct username and password, so we can go ahead and authenticate them in our app too.

OAuth will make our life a lot easier when it comes to third-party login options such as logging in with Google or Facebook. With OAuth, we will have less liability and this is the way that many websites only allow this type of login. Although we need to learn about OAuth to implement these changes, it will be worth it in the end!

What exactly is special about OAuth? Why OAuth?
as there are a lot of other open standards that do something similar to these;

OAuth is quite special in three ways:

Granular Access Levels: Granular access means that when a user logs in with Facebook, you can request specific information from their account. So, for example, if you only need their profile and email address for your app, you can request that data accordingly. This allows apps to only request the data they need, which helps protect user privacy.

Read or Read + Write Access: it allows for either Read Only or Read and Write Access. So in the case of Facebook, this means that we can either ask them to just retrieve pieces of information about their Facebook account like their name, email, and friends list. Or we can ask for write access as well. Say for example in our previous case if our blog app wanted to be able to post to Facebook on this user's account then we would need to ask for read-and-write access.

Revoke Access: The third-party service we're using to authenticate our users must give them the ability to revoke access at any time. For example, if we're authenticating with Facebook, the user should be able to go into their Facebook account and de-authorize the access they granted to our website. This way, they don't have to go onto our site and potentially struggle to remove our access.

So now that we've looked at what's special about OAuth, the next thing to talk about is, well...

How does it work in reality?
Step 1: Set Up Our App

The first step is to tell Facebook, GitHub or Google about our Web application. We have to set up our app in their developer console and return, we get an App ID or Client ID. Our website is then the client who will make requests to Facebook to authenticate our users.

Step 2: Redirect to Authenticate

The next step in the process occurs when the user visits our blog app and attempts to log in using their Facebook credentials. By giving the user the option to log in with Facebook, we streamline the process and make it more convenient for them.

Step 3: User Logs In

We'll take users to the Facebook website when they click on the Facebook option, so they can log in using their Facebook credentials. This way, they'll be seeing a familiar and trustworthy interface.

If we didn't have OAuth, we would have to ask users for their login credentials for Facebook, which would seem sketchy and insecure. OAuth makes that process a lot easier by allowing users to log in to the website they trust (Facebook) using credentials they're already familiar with.

Step 4: User Grants Permissions

When a user logs into our website from a third-party site, they will be prompted to review the permissions that our website is requesting. For example, we might want their profile and email address. If they're OK with granting us that permission, they click "allow."

Step 5: Receive the Authorization code

So now that they've granted us permission and successfully logged in on Facebook, our website will receive an authorization code. This allows us to check if the user has signed in to Facebook with the correct credentials. If everything checks out, we're then able to authenticate the user and log them into our website.

Step 6: Exchange AuthCode for Access Token

If we wanted to go a step further, we can exchange our authentication code for an access token. And when we receive that access token from Facebook, we would save it into our database because this is the token that we can use if we want to request pieces of information subsequently.

The access token is valid for a lot longer than the authentication token, so we can think of the authentication code or OAuth code as being like a ticket. It's a ticket that we're only going to use once to get into the cinema.

An access token is a lot like a year-long pass to an amusement park. It allows you to request data from Facebook that the user has allowed you to access, such as their friend list, username, or password.

The OAuth code is what we use to authenticate a user who has successfully logged in through Facebook. The access token is what we'll use to access information that is stored on that user's account, such as their email or friend's list.

Now that we know all of this, let's go ahead and put it into practice. We're going to be implementing login with Google, Facebook, and Github using Passport.js and Google OAuth, Facebook Outh, and GitHub OAuth inside our Express app.

Complete Step By Step Implementation article [here](https://wulfi.hashnode.dev/a-step-by-step-guide-to-oauth-20-implementing-sign-in-with-google-facebook-and-github).