FROM golang:latest

# Set up octobot's environment
COPY . /bot/ogame
WORKDIR /bot/ogame

RUN go get "github.com/alaingilbert/ogame" && go build -o main .

ENTRYPOINT ["/bot/ogame/main"]