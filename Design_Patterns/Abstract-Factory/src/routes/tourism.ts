import { Hono } from "hono";
import { Variables } from "../types";
import { getHotels } from "../types";
import { getActivities } from "../daos/get-flights";
import { AmadeusFactory } from "../factories/AmadeusFactory";

const tourismRouter = new Hono<{ Variables: Variales}