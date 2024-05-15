1.Open VSCode and create a new Python file.
2.Copy the code provided into the Python file.
3.Replace 'YOUR_API_KEY' with your actual Alpha Vantage API key.
4.Save the file with a .py extension, for example, stock_portfolio.py.
5.Install the requests module if you haven't already by running pip install requests in the terminal.
6.Open a terminal in VSCode by selecting Terminal > New Terminal.
7.Navigate to the directory where your Python file is located using the cd command.
8.Run the script by typing python stock_portfolio.py in the terminal and press Enter.

The script should execute, and you should see the output displaying the portfolio with the current stock prices.

#This will execute the script, and you should see the output displaying the portfolio with the current stock prices.

 You can easily obtain an API key by signing up on their website. Here's how you can do it:

Visit the Alpha Vantage website: [Alpha Vantage](https://www.alphavantage.co/).
Click on the "Get your free API key" button.
Sign up for an account by providing your email address and choosing a password.
Once you're signed in, you'll be able to generate an API key.
Copy the API key and use it in your code to access Alpha Vantage's API services.
Make sure to keep your API key secure and don't share it publicly in your code or elsewhere to prevent unauthorized access to your account and potential misuse of the service.

##NOTE

In this simplified version, I condensed the add_stock method to use the dict.get() method to avoid repetitive code. 
Make sure to replace 'YOUR_API_KEY' with your actual Alpha Vantage API key before running the script.
