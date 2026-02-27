def main():
    from core.imageCleaner import clean_images
    from logger.loggerSetup import setupLogger

    #setup logger to show logs in terminal and log files
    setupLogger();
    # method to generate clean image(s) and metadata text file(s)
    clean_images();

if __name__ == "__main__":
    main()