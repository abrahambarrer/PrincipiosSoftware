import com.example.urlbuilder.*

fun main() {
    val urlBuilder = URLBuilder()

    val url1 = urlBuilder.setProtocol("http")
        .setHostname("newwebsite")
        .setPort("43")
        .addPath("example")
        .addPath("proko")
        .addPath("pako")
        .addQueryParam("name", "John Doe")
        .addQueryParam("city", "Mexico")
        .build()

    println(url1)

    val urlDirector = URLManager(urlBuilder)
    val url2 = urlDirector.buildSearchUrl(
        host = "example",
        query = "ping",
        page = 100
    )

    println(url2)
}