package main

import (
	"github.com/kataras/iris/v12"
	"github.com/kataras/iris/v12/middleware/logger"
	"github.com/kataras/iris/v12/middleware/recover"
)

func main() {
	app := iris.New()
	app.Logger().SetLevel("debug")
	app.Use(recover.New())
	app.Use(logger.New())
	app.Get("/", func (ctx iris.Context){
		ctx.HTML("Hello")
	})


	app.Run(iris.Addr(":8080"), iris.WithoutServerError(iris.ErrServerClosed))
}
