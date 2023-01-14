from Tests import loggerTest, qrcodeTest, instagramTest, youtubeTest

results = []
results.append(loggerTest.testingLogInfo())
results.append(loggerTest.testingLogDebug())
results.append(loggerTest.testingLogError())
results.append(qrcodeTest.testingQRCodeWrite())
results.append(instagramTest.checkIfFailedDownloadPostNotFound())
results.append(instagramTest.testingInstagramDownloadImagePost())
results.append(youtubeTest.testingYoutubeDownloadVideo())

for result in results:
    if result != 200:
        print(result)