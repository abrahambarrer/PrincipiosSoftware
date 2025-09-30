import com.example.urlbuilder.*

fun main() {
    val urlbuilder = URLBuilder()

    val url1 = urlbuilder.setProtocol("http")
        .setHostname("newwebsite")
        .setPort("43")
        .addPath("example")
        .addPath("proko")
        .addPath("pako")
        .addQueryParam("name", "John Doe")
        .addQueryParam("city", "Mexico")
        .build()

    println(url1)

    val urldirector = URLManager(urlbuilder)
    val url2 = urldirector.buildSearchUrl(
        host = "example",
        query = "ping",
        page = 100
    )

    println(url2)
}