package main
import (
    "fmt"
    "flag"
    "github.com/dghubble/go-twitter/twitter"
    "github.com/dghubble/oauth1"
    "os"
)
func main(){
	var handle string    
	fmt.Println("Users Handle")
	fmt.Scanln(&handle)
	var test=flag.String("Users Handle",handle,"It is the users handle for which we require information.") 
	flag.Parse()
	config := oauth1.NewConfig("koNrY5Rw4P7XqQNXnRM9hhmG4", "0qrhgRMusoy9WYILFj2D41pqtuDIUOaTOZC2NKY6hi0bp1fNtm")
	token := oauth1.NewToken("1170003422830940161-WRN740jqRwhvtmrfHJT3pyELZJgLF3", "ZSyczgMCQDICd6FjupFDo5kxWDsIoee0MUEujwJFjeyfz")
	httpClient := config.Client(oauth1.NoContext, token)
	client := twitter.NewClient(httpClient)
	params := &twitter.FollowerListParams{
        ScreenName: *test,
       }
	followers, resp, err := client.Followers.List(params)
	f, err := os.Create("Randomn.txt")
        if err != nil {
           fmt.Println(err)
           return
        }
	var i int=0
	fmt.Println(resp, err)
	f.WriteString("The given user has the following followers " + *test)
	for _, follower := range followers.Users {
		i=i+1
		f.WriteString("\n" + follower.ScreenName)
	}
	f.WriteString("\n")
        f.Close()
	

}
