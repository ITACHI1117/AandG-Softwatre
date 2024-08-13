def run_auto_update(load_dotenv,os,push_Sdate,push_Edate,error_message,
                    Reg_update_button,auto_push,run,SHOW_WINDOW,write_logs,
                    write_last_push_date,delete_last_push_date,time,continue_push,delete):
    # enviroment variables
    load_dotenv()
    THIRD_PARTY_PLATFORM_LINK = os.getenv("3RD_PARTY_PLATFORM_LINK")
    THIRD_PARTY_PLATFORM_EMAIL = os.getenv("3RD_PARTY_PLATFORM_EMAIL")
    THIRD_PARTY_DETAILS = [THIRD_PARTY_PLATFORM_LINK, THIRD_PARTY_PLATFORM_EMAIL]
    push_Sdate
    push_Edate
    error_message.config(text=f"Starting👩‍💻...", bootstyle="success")
    Reg_update_button.config(state="disabled")
    auto_push.config(state="disabled")
    try:
        error_message.config(text=f"Pushing👩‍💻...", bootstyle="success")
        # running push
        Pushing_dates = run("01-07-Jul", "05-07-Jul", SHOW_WINDOW, THIRD_PARTY_DETAILS)
        for Pushing_date in Pushing_dates:
            error_message.config(text=f"Pushed {Pushing_date[0]} to {Pushing_date[1]}", bootstyle="success")
            print(f"pushed {Pushing_date[0]} to {Pushing_date[1]}")
            write_logs(Pushing_date[0], Pushing_date[1], Pushing_date[2])
            push_Sdate = Pushing_date[3]
            push_Edate = Pushing_date[4]
            print(push_Sdate, push_Edate)
            write_last_push_date(push_Sdate, push_Edate)
        error_message.config(text=f"Done✅", bootstyle="success")
        delete_last_push_date()
        time.sleep(10)
        error_message.config(text=f"", bootstyle="success")
        continue_push.config(state="disabled")
        return push_Sdate, push_Edate
    except Exception as e:
        # writing the last push date so for the continue function
        write_last_push_date(push_Sdate, push_Edate)
        print(e)
        # deleting the niid file
        delete()
        continue_push.config(state="enabled")
        error_message.config(text=f"There was an error", bootstyle="danger")
        Reg_update_button.config(state="enabled")
        auto_push.config(state="enabled")
        time.sleep(10)
        error_message.config(text=f"", bootstyle="danger")
        return push_Sdate, push_Edate
    finally:
        Reg_update_button.config(state="enabled")
        auto_push.config(state="enabled")