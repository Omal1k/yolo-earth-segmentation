# yolo-earth-segmentation



## to run model:
```
docker run -p 1234:1234 omalik26/yolo-segment-earth:latest
```

## How to send request:

```
curl -X POST \
  -F "file=@path/to/your/image.jpg" \
  -o path_to_image \
  http://localhost:1234/segment
```
