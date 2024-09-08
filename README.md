# Time to Distance Converter

This Streamlit app allows users to convert a given time duration into the equivalent distance that a car would travel, based on predefined speed assumptions for different time intervals.

Open tool here: https://time-to-distance.streamlit.app

## Features

- **Time Input**: Users can input the duration for which the car has been driving.
- **Unit Selection**: Users can select the unit of time (seconds, minutes, hours, or days).
- **Distance Calculation**: The app calculates the distance driven based on the input time and unit, using specified speed rules for different time periods.
- **Interactive Interface**: A button is provided to trigger the conversion and display the result.

## Speed Assumptions

The app uses the following speed assumptions for different time intervals:

- **Seconds**: Constant speed of 5 mph, converted to miles per second.
- **Minutes**:
  - 0 to 20 minutes: 30 mph
  - Over 20 minutes: 60 mph
- **Hours**:
  - 0 to 1 hour: 50 mph
  - 1 to 10 hours: 65 mph
  - Over 10 hours: 70 mph
- **Days**: Constant speed of 70 mph, converted to miles per day.

## How to Use

1. **Installation**:

   - Ensure you have Python installed.
   - Install Streamlit using pip:
     ```bash
     pip install streamlit
     ```

2. **Run the App**:

   - Save the app code in a file, e.g., `app.py`.
   - Run the app using the command:
     ```bash
     streamlit run app.py
     ```

3. **Interact with the App**:
   - Enter the time duration and select the corresponding unit.
   - Click the "Convert" button to see the calculated distance.

## Future Enhancements

- Add a graphical representation of speed vs. time.
- Allow users to input custom speed rules.
- Enhance the UI for better user experience.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README provides a concise overview of the app, detailing its functionality, usage instructions, and potential future enhancements. Adjust the content as needed to better fit your specific app details and goals.
