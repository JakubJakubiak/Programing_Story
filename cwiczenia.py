import cv2
import numpy as np

# capture = cv2.VideoCapture(0)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# faceCascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

# cv::dnn::dnn4_v20220524::readNetFromDarknet("/path/to/openpose.cfg")


# import sys
# sys.path.append('/usr/local/python')
# from  openpose  import pyopenpose as op


# https://github.com/infocom-tpo/tf-openpose/blob/master/README.md

# Wczytujemy model OpenPose
net = cv2.dnn.readNet("openpose.weights", "openpose.cfg")

# Ustawiamy nazwy warstw w modelu OpenPose
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Uruchamiamy kamerę
capture = cv2.VideoCapture(0)


while True:
    # Pobieramy klatkę z kamery
    _, frame = capture.read()
    height, width, channels = frame.shape

    # Tworzymy obiekt typu "blob" z klatki z kamery
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)

    # Wstawiamy "blob" do sieci neuronowej
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Pobieramy współrzędne punktów na ciele
    points = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Jeśli pewność wykrycia jest wystarczająco wysoka
            if confidence > 0.5:
                # Pobieramy współrzędne punktów na ciele
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Pobieramy współrzędne lewego górnego i prawego dolnego rogu prostokąta otaczającego ciało
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                points.append((x, y))

    # Jeśli zostały znalezione co najmniej trzy punkty na ciele
    if len(points) >= 3:
        # Sprawdzamy, czy użytkownik wykonuje przysiady
        if points[5][1] > points[0][1] and points[5][1] > points[1][1] and points[5][1] > points[2][1]:
            print('Przysiady')

        # Sprawdzamy, czy użytkownik podnosi hantle
        elif points[7][1] < points[4][1] and points[7][1] < points[5][1] and points[7][1] < points[6][1]:
            print('Podnoszenie hantli')

        # W przeciwnym wypadku u

    while True:
        # Pobieramy klatkę z kamery
        _, frame = capture.read()
        height, width, channels = frame.shape

        # Tworzymy obiekt typu "blob" z klatki z kamery
        blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)

        # Wstawiamy "blob" do sieci neuronowej
        net.setInput(blob)
        outs = net.forward(output_layers)

        # Pobieramy współrzędne punktów na ciele
        points = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                # Jeśli pewność wykrycia jest wystarczająco wysoka
                if confidence > 0.5:
                    # Pobieramy współrzędne punktów na ciele
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Pobieramy współrzędne lewego górnego i prawego dolnego rogu prostokąta otaczającego ciało
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    points.append((x, y))

        # Jeśli zostały znalezione co najmniej trzy punkty na ciele
        if len(points) >= 3:
            # Sprawdzamy, czy użytkownik wykonuje przysiady
            if points[5][1] > points[0][1] and points[5][1] > points[1][1] and points[5][1] > points[2][1]:
                print('Przysiady')

            # Sprawdzamy, czy użytkownik podnosi hantle
            elif points[7][1] < points[4][1] and points[7][1] < points[5][1] and points[7][1] < points[6][1]:
                print('Podnoszenie hantli')

            # W przeciwnym wypadku użytkownik nie wykonuje żadnych znanych ćwiczeń
            else:
                print('Brak wykrytych ćwiczeń')

        # Wyświetlamy klatkę z k
        ...

        # while True:
        #     # Pobieramy klatkę z kamery
        #     _, frame = capture.read()
        #     height, width, channels = frame.shape

        #     # Tworzymy obiekt typu "blob" z klatki z kamery
        #     blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)

        #     # Wstawiamy "blob" do sieci neuronowej
        #     net.setInput(blob)
        #     outs = net.forward(output_layers)

        #     # Pobieramy współrzędne punktów na ciele
        #     points = []
        #     for out in outs:
        #         for detection in out:
        #             scores = detection[5:]
        #             class_id = np.argmax(scores)
        #             confidence = scores[class_id]

        #             # Jeśli pewność wykrycia jest wystarczająco wysoka
        #             if confidence > 0.5:
        #                 # Pobieramy współrzędne punktów na ciele
        #                 center_x = int(detection[0] * width)
        #                 center_y = int(detection[1] * height)
        #                 w = int(detection[2] * width)
        #                 h = int(detection[3] * height)

        #                 # Pobieramy współrzędne lewego górnego i prawego dolnego rogu prostokąta otaczającego ciało
        #                 x = int(center_x - w / 2)
        #                 y = int(center_y - h / 2)

        #                 points.append((x, y))

        #     # Jeśli zostały znalezione co najmniej trzy punkty na ciele
        #     if len(points) >= 3:
        #         # Sprawdzamy, czy użytkownik wykonuje przysiady
        #         if points[5][1] > points[0][1] and points[5][1] > points[1][1] and points[5][1] > points[2][1]:
        #             print('Przysiady')

        #         # Sprawdzamy, czy użytkownik podnosi hantle
        #         elif points[7][1] < points[4][1] and points[7][1] < points[5][1] and points[7][1] < points[6][1]:
        #             print('Podnoszenie hantli')

        #         # W przeciwnym wypadku użytkownik nie wykonuje żadnych znanych ćwiczeń
        #         else:
        #             print('Brak wykrytych ćwiczeń')

        #     # Wyświetlamy klatkę z k

