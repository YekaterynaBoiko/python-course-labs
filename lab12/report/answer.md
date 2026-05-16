# Answer for questions
## 1.
Unit tests are tests that check a single function separately from the rest of the system. We don’t run the whole application, we just test one small part of the code, like ***process_item***. The focus is only on input and output of that function. 

Behavior tests check the whole program as a system. We run it the same way a user would, for example through the CLI command, and we check if everything works together correctly: file reading, task processing, and JSON output.

## 2.
Subprocess is used because we need to test the CLI as a real separate program, not just Python functions. So we run it using a command like **python -m ...**, just like a user would do in the terminal. 

This allows us to check real behavior: output, exit code, and how command-line arguments work.

## 3.
If one async task fails and there is no error handling, the whole group of tasks can fail. For example, with ***asyncio.gather***, one exception can stop all other tasks from finishing. 

So instead of processing everything, the program may crash or stop early because of one error.

## 4.
You test internal functions when you want to check specific logic in isolation. For example, **process_item** is a simple function, so it makes sense to test it directly. 

You test full system behavior when you want to make sure all parts work together. For example, running the CLI, reading JSON files, executing tasks, and printing output correctly.

## 5. 
Time-based tests can be unstable because they depend on execution speed. Sometimes they pass, sometimes they fail depending on the machine load or environment. 

They also slow down the test suite because you need to wait for delays like sleep. That’s why they are considered flaky and are usually avoided when possible.