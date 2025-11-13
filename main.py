import json
import livef1

def main():
    print("Hello from f1-batch-streaming-data!")

    # session = livef1.get_session(
    #     season=2025,
    #     meeting_identifier="Montreal",
    #     session_identifier="Race"
    # )

    # position_data = session.get_data(
    #     dataNames="Position.z"
    # )

    # print(position_data.head())

    season = livef1.get_season(season=2024)

    print(type(season))

if __name__ == "__main__":
    main()
